import time
import json
import arrow
import dataclasses
from typing import Union
from notion_client import Client
from pymstodo import ToDoConnection

with open("./config.json") as f:
    config = json.load(f)

client_id, client_secret, notion_secret, database_id = config["env"]

auth_url = ToDoConnection.get_auth_url(client_id)
redirect_resp = input(
    f"Go here and authorize:\n{auth_url}\n\nPaste the full redirect URL below:\n"
)
token = ToDoConnection.get_token(client_id, client_secret, redirect_resp)
todo_client = ToDoConnection(
    client_id=client_id, client_secret=client_secret, token=token
)

notion_client = Client(auth=notion_secret)


@dataclasses.dataclass
class DatabaseItem:
    title: str
    importance: bool
    list_name: str
    due_time: Union[str, None]
    note: str
    note_type: str

    def json(self) -> dict:
        if self.due_time is None:
            return {
                "Name": {"title": [{"text": {"content": self.title}}]},
                "Importance": {"checkbox": self.importance},
                "List": {"select": {"name": self.list_name}},
                "Due Time": {"date": None},
                "Note": {
                    "rich_text": [{"text": {"content": self.note if self.note_type == "text" else ""}}]
                },
            }
        else:
            return {
                "Name": {"title": [{"text": {"content": self.title}}]},
                "Importance": {"checkbox": self.importance},
                "List": {"select": {"name": self.list_name}},
                "Due Time": {"date": {"start": arrow.get(self.due_time).to('Singapore').isoformat()}},
                "Note": {
                    "rich_text": [{"text": {"content": self.note if self.note_type == "text" else ""}}]
                },
            }


if __name__ == "__main__":
    while True:
        task_name = []
        for task_list in todo_client.get_lists():

            for task in todo_client.get_tasks(task_list.list_id, status="notCompleted"):
                task_name.append(task.title)
                item = DatabaseItem(
                    task.title,
                    True if task.importance == "high" else False,
                    task_list.displayName,
                    None if task.dueDateTime is None else task.dueDateTime["dateTime"],
                    task.body["content"],
                    task.body["contentType"]
                )
                r = notion_client.databases.query(
                    database_id,
                    filter={"property": "Name", "title": {"equals": task.title}},
                )
                if len(r["results"]) == 0:
                    notion_client.pages.create(
                        parent={"database_id": database_id}, properties=item.json()
                    )
                else:
                    page_id = r["results"][0]["id"]
                    notion_client.pages.update(page_id, properties=item.json())

        for entry in notion_client.databases.query(
                    database_id)["results"]:
            if entry["properties"]["Name"]["title"][0]["plain_text"] not in task_name:
                notion_client.pages.update(entry["id"], archived=True)
        
        time.sleep(90)
