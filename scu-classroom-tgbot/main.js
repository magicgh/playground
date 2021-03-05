const TelegramBot = require('node-telegram-bot-api');
const token = "YOUR_TOKEN";
const bot = new TelegramBot(token, {polling: true});
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var jxl_map=new Map([['东二教','WJdong2'],['东三教','WJdong3'],['基教楼A座','WJjijiaoA'],['基教楼C座','WJjijiaoC'],['一教A座','yjA'],['一教B座','yjB'],['一教C座','yjC'],['一教D座','yjD'],['综合楼B座','zongB'],['综合楼C座','zongC'],['文科楼一区','wen1'],['文科楼二区','wen2'],['文科楼三区','wen3'],['九教','HX9'],['十教','HX10'],['研究生院','WJyjs']]);

bot.onText(/\/start/,msg=>{
    bot.sendMessage(msg.chat.id, "选择校区:",{
        "reply_markup":{
            "keyboard":[["望江"],["华西"],["江安"]]
        }
    });
});

bot.on('message',(msg)=>{
    if(msg.text==="望江"){
        bot.sendMessage(msg.chat.id, "选择教学楼:",{
            "reply_markup":{
                "keyboard":[["东二教","东三教"],["基教楼A座","基教楼C座"],["研究生院"]]
            }
        });

    }
    if(msg.text==="华西"){
        bot.sendMessage(msg.chat.id, "选择教学楼:",{
            "reply_markup":{
                "keyboard":[["九教"],["十教"]]
            }
        });
    }
    
    if(msg.text==="江安"){
        bot.sendMessage(msg.chat.id, "选择教学楼:",{
            "reply_markup":{
                "keyboard":[["一教A座","一教B座","一教C座"],["一教D座","综合楼B座","综合楼C座"],["文科楼一区","文科楼二区","文科楼三区"]]
            }
        });
    }
});

bot.on('message',(msg)=>{
    if(jxl_map.has(msg.text)){
        var bj=0;
        var cr_map=new Map();
        var cr_list=[];
        var xhr = new XMLHttpRequest();
        var result=null;
        xhr.open("POST","http://cir.scu.edu.cn/cir/XLRoomData", false);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
        xhr.responseType="json";
        xhr.onload= function(){
            if(this.readyState===4)result=this.responseText;
        };
        xhr.send("jxlname="+jxl_map.get(msg.text));
        for (x of JSON.parse(result).roomdata){
            cr_map.set(x.roomName,x.classUse);
            cr_list.push(x.roomName);
        }

        bot.sendMessage(msg.chat.id, `${msg.text}的所有教室如下：${cr_list}`);
        bot.sendMessage(msg.chat.id, '输入教室：');
        bot.on('message',(msg)=>{
            if(cr_map.has(msg.text)&&!bj){
                bj=1;
                for (let i=1;i<=5;i++){
                    cr_status=cr_map.get(msg.text)[i-1].kcm;
                    bot.sendMessage(msg.chat.id, `第${i}节：${cr_status===null?"空":cr_status}`);
                }
            }
        });
    }
    
});
