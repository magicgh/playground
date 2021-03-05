from manimlib.imports import *
class StartScene(Scene):
    def construct(self):
        title=TextMobject("\\textbf{Solar Sail Craft}")
        en_title=title.copy().set_color(ORANGE).to_edge(UP*2.5).scale(2.5)
        cn_title=TextMobject("\yahei{太 \space 阳 \space 帆 \space 飞 \space 船}").next_to(en_title,DOWN,buff=0.5).scale(1.5)
        intro=TextMobject("\\textrm{Introduction}").set_color(YELLOW)
        prin=TextMobject("\\textrm{Principle}").set_color(GREEN)
        demo=TextMobject("\\textrm{Demonstration}").set_color(BLUE)
        chapter=VGroup(intro,prin,demo).arrange(DOWN).to_edge(DOWN*2.5).scale(1.5)
        title.bg= SurroundingRectangle(title,color=ORANGE,fill_color=ORANGE,fill_opacity=0.5)
        title_group=VGroup(title.bg,title)
        line = Line(np.array([-3,0,0]), np.array([4.5,0,0]), color=ORANGE)
        piCreature = PiCreature(color=ORANGE,height = 1).next_to(line, LEFT)
        self.play(GrowFromCenter(piCreature),run_time=1)
        for dre in [UP,LEFT,DOWN,RIGHT]:
            self.play(ApplyMethod(piCreature.look,dre),run_time=0.85)
        piCreature.look_at(line)
        self.play(ShowCreation(line), Blink(piCreature))
        self.wait(0.2)
        self.play(ReplacementTransform(line,title_group),run_time=0.6)
        self.wait(0.5)
        self.play(Transform(title_group,en_title),Blink(piCreature),run_time=0.6)
        self.wait(0.5)
        self.play(Transform(en_title,cn_title),Blink(piCreature),ReplacementTransform(piCreature,chapter))
        self.wait(2)
        def mob_move(mob):
            mob.scale(1.5)
            mob.set_color(WHITE)
            mob.move_to(ORIGIN)
            return mob
        self.play(FadeOutAndShift(title_group,UP),FadeOutAndShift(en_title,UP),\
        FadeOutAndShift(demo,DOWN),FadeOutAndShift(prin,DOWN),\
        ApplyFunction(mob_move,intro))
        self.play(WiggleOutThenIn(intro))
        self.wait(0.2)
        self.play(FadeOut(intro))

class IntroScene(Scene):
    speech_dir=os.path.join('D:\\','Software','manim-master','manimlib','files','Bubbles_speech.svg')
    sci_dict={
        "\\textsc{Johannes Kepler}":"\\RaggedRight \\textsl{\\quad observed that comet tails point away from the Sun \\\ and suggested that the Sun caused the effect.}",
        "\\textsc{James Clerk Maxwell}":"\\RaggedRight \\textsl{\\quad His equations provide the theoretical foundation \\\ for sailing with light pressure.}",
        "\\textsc{Pyotr Lebedev}":"\\textsl{successfully demonstrate light pressure \\\ with a torsional balance.}",
        "\\textsc{Konstantin Tsiolkovsky}":"\\textsl{\\quad first proposed using the pressure of sunlight \\\ to propel spacecraft through space.}",
        "\\textsc{Friedrich Zander}":"\\textsl{\\quad wrote of ``applying small forces\'\' \\\ \
        using ``light pressure or transmission of light energy\\\ to distances by means of very thin mirrors\'\'.}",
        "\\textsc{JBS Haldane}":"\\textsl{speculated how ``wings of metallic foil \\\ of a square kilometre or more in area are \
        \\\ spread out to catch the Sun's radiation pressure\'\'.}",
    }   
    def picContact(self):
        left_pic=PiCreature(color=ORANGE,height = 1).to_edge(LEFT+5*DOWN)
        right_pic=PiCreature(color=YELLOW,height = 1).to_edge(RIGHT+5*DOWN)
        question=Bubble(file_name=self.speech_dir).scale(0.5)
        question.txt=TextMobject('What is solar sail?')
        question.add_content(question.txt).scale(1.1)
        question.group=VGroup(question,question.txt).next_to(left_pic,UR,buff=0.1)
        ans=Bubble(file_name=self.speech_dir).flip()
        ans.txt=VGroup(TextMobject('A method of spacecraft propulsion'),\
                TextMobject('using radiation pressure'),\
                TextMobject('exerted by sunlight'),\
                TextMobject('on large mirrors.')).arrange(DOWN)
        ans.add_content(ans.txt).scale(1.1)
        ans.group=VGroup(ans,ans.txt).scale(0.75).next_to(right_pic,UL,buff=0.1)
        left_pic.make_eye_contact(right_pic)
        right_pic.make_eye_contact(left_pic)
        self.play(FadeIn(left_pic),FadeIn(right_pic))
        self.wait(0.5)
        self.play(Write(question.group),Blink(left_pic))
        self.wait(0.5)
        self.play(Write(ans.group),Blink(right_pic),run_time=5)
        self.wait()
        addition=Bubble(file_name=self.speech_dir).flip()
        addition.txt=VGroup(TextMobject('Based on the physics,'),\
                TextMobject('a number of spaceflight missions'),\
                TextMobject('to test solar propulsion and navigation'),\
                TextMobject('have been proposed since the 1980s.')).arrange(DOWN)
        addition.add_content(addition.txt).scale(1.1)
        addition.group=VGroup(addition,addition.txt).scale(0.75).next_to(right_pic,UL+DOWN*0.9,buff=0.05)
        self.play(ReplacementTransform(ans.group,addition.group),Blink(right_pic),run_time=0.5)
        self.wait(3.5)
        self.play(*[FadeOut(mob) for mob in [left_pic,right_pic,question.group,addition.group]])
        
    def historyIntro(self):
        title=TextMobject('\\textbf{History of Concept}').set_color(YELLOW)
        piCreature=PiCreature(color=ORANGE,height = 1).to_corner(DL)
        self.play(ShowCreation(title),run_time=1.5)
        self.wait(0.5)
        self.play(ApplyMethod(title.to_corner,UL),GrowFromPoint(piCreature,title.get_center()))
        piCreature.look(ORIGIN)
        for name,incident in self.sci_dict.items():
            mob_inc=TextMobject(incident).set_color(GRAY).to_edge(ORIGIN)
            mob_name=TextMobject(name).next_to(mob_inc,UP,buff=0.5)
            self.play(FadeInFrom(mob_name,UP),FadeInFrom(mob_inc,UP))
            self.wait(0.5)
            self.play(Indicate(mob_name),Blink(piCreature))
            self.wait(1.5)
            self.play(FadeOutAndShiftDown(mob_name),FadeOutAndShiftDown(mob_inc))
        so_on=TextMobject('... ...')
        prin_title=TextMobject("\\textrm{Principle}").set_color(GREEN).scale(1.5)
        self.play(Write(so_on))
        self.wait(0.5)
        self.play(FadeOut(title),FadeOut(piCreature),ReplacementTransform(so_on,prin_title))
        self.wait(1)
        self.play(FadeOut(prin_title))

    def construct(self):
        self.picContact()
        self.historyIntro()

class PrinScene(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -10,
        "y_max": 10,
        "x_axis_width": 10,
        "y_axis_height": 10,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "graph_origin":ORIGIN+DOWN+2*LEFT,
        "x_axis_label": None,
        "y_axis_label": None,
        "axes_color": None,
    }
    speech_dir=os.path.join('D:\\','Software','manim-master','manimlib','files','Bubbles_speech.svg')
    def picContact(self):
        left_pic=PiCreature(color=ORANGE,height = 1).to_edge(LEFT+5*DOWN)
        right_pic=PiCreature(color=GREEN,height = 1).to_edge(RIGHT+5*DOWN)
        question=Bubble(file_name=self.speech_dir).scale(0.5)
        question.txt=TextMobject('How it works?')
        question.add_content(question.txt).scale(1.1)
        question.group=VGroup(question,question.txt).next_to(left_pic,UR,buff=0.1)
        ans=Bubble(file_name=self.speech_dir).scale(0.5).flip()
        ans.txt=TextMobject('Let me show you.')
        ans.add_content(ans.txt).scale(1.1)
        ans.group=VGroup(ans,ans.txt).next_to(right_pic,UL,buff=0.1)
        left_pic.make_eye_contact(right_pic)
        right_pic.make_eye_contact(left_pic)
        self.play(FadeIn(left_pic),FadeIn(right_pic))
        self.wait(0.5)
        self.play(Write(question.group),Blink(left_pic))
        self.wait()
        self.play(Write(ans.group),Blink(right_pic))
        self.wait()
        self.play(*[FadeOut(mob) for mob in [left_pic,right_pic,question.group,ans.group]])

    def showPrin(self):
        self.setup_axes()   
        c2p=self.coords_to_point
        body=Polygon(*[c2p(x,y) for x,y in [(-1.5,1),(1.5,1),(1,0),(-1,0)]],color=GREEN)
        sail=Line(*[c2p(x,y) for x,y in [(0,1),(0,4)]]).set_color(GREEN)
        ship=VGroup(body,sail)
        ship_label=TextMobject('Solar Sail Model').scale(0.7).next_to(ship,DOWN)
        init_ang=-80*DEGREES #must be negative
        force_ang=init_ang+45*DEGREES
        lit_ang=ValueTracker(init_ang)
        start_point=c2p(4*np.cos(init_ang),2.5+4*np.sin(init_ang))
        force_start=end_point=sail.get_center()
        force_end=c2p(4,2.5)
        inc_lit=Arrow(start_point,end_point).set_color(GOLD)
        act_point=SmallDot().move_to(sail.get_center())
        grid=NumberPlane()
        delta=0
        def inc_conf(obj):
            obj.set_angle_ap(lit_ang.get_value(),end_point)

        inc_lit.add_updater(inc_conf)
        ref_lit=Arrow(end_point,start_point).set_color(GOLD)

        def ref_conf(obj):
            ang_v=lit_ang.get_value()
            obj.set_angle_ap(-PI-ang_v+delta,end_point)

        ref_lit.add_updater(ref_conf)
        force=Arrow(force_start,force_end).set_color(WHITE)
        force_label=TexMobject('F')

        def force_label_conf(obj):
            obj.next_to(force.get_end(),RIGHT)
            
        force_label.add_updater(force_label_conf)
        inc_label=TexMobject('Light').set_color(GOLD).next_to(inc_lit.get_start(),UL,buff=0.1)
        force_txt=TexMobject(r'=\frac{2P_{0}}{c}').next_to(force_label,RIGHT)
        angle_label=TextMobject('Angle =').next_to(ship,10*RIGHT+4*UP)
        angle_val = DecimalNumber(
            lit_ang.get_value(),
            show_ellipsis=False,
            num_decimal_places=4,
            include_sign=False,
        ).next_to(angle_label,RIGHT).add_updater(lambda m: m.set_value(lit_ang.get_value()))
        self.play(GrowFromEdge(ship,LEFT))
        self.wait(0.5)
        self.play(Write(ship_label))
        self.wait(0.3)
        self.play(FadeOut(ship_label))
        self.wait(0.2)
        self.play(ShowCreation(inc_lit),Write(inc_label),ShowCreation(ref_lit),run_time=1)
        self.wait(0.1)
        self.play(FadeIn(act_point),ShowCreation(force),Write(force_label))
        self.wait(0.2)
        self.play(FadeOut(inc_label),Write(force_txt))
        self.wait(0.5)
        self.play(ReplacementTransform(force_txt,angle_label))
        self.wait(0.1)
        self.play(Write(angle_val),run_time=0.5)
        self.wait(0.5)
        self.play(ApplyMethod(lit_ang.set_value,-init_ang),run_time=1)
        self.wait(0.2)
        self.play(ApplyMethod(lit_ang.set_value,-55*DEGREES),run_time=1)
        self.wait(0.5)

        tip_angle=60*DEGREES
        tip_sail=sail.copy()
        tip_sail.set_angle(tip_angle)
        tip_center=tip_sail.get_center()
        tip_inc=inc_lit.copy().move_to(tip_center-inc_lit.get_vector()*0.5)
        tip_ref=ref_lit.copy().move_to(tip_center+ref_lit.get_vector()*0.5)

        self.play(*([ReplacementTransform(x,y) for x,y in [(sail,tip_sail),(inc_lit,tip_inc)]]\
            +[FadeOut(obj) for obj in [ref_lit,force,force_label,act_point]]),run_time=0.5)
        act_point.move_to(tip_center)
        end_point=tip_center
        delta=300*DEGREES
        force.move_to(tip_center+force.get_vector()*0.5)
        force.rotate_about_ap(-PI/6,tip_center)

        self.play(*[FadeIn(obj) for obj in [tip_ref,force,force_label,act_point]],run_time=0.5)
        self.play(ApplyMethod(lit_ang.set_value,55*DEGREES),run_time=1)
        self.wait(0.2)
        self.play(ApplyMethod(lit_ang.set_value,-55*DEGREES),run_time=1)
        self.wait(0.5)

        orbit_radius=6
        delta_x,delta_y=0,2
        sail_group=VGroup(body,tip_sail,tip_inc,tip_ref,force,force_label,act_point)
        craft=Rectangle(height=0.4,width=0.2,color=GREEN).move_to(c2p(orbit_radius,delta_y))

        def build_orbit(theta):
            x=orbit_radius*np.cos(theta)+delta_x
            y=orbit_radius*np.sin(theta)+delta_y
            return x,y

        orbit=self.get_parameterized_graph(build_orbit,color=LIGHT_BROWN)
        sun=Circle().move_to(c2p(delta_x,delta_y)).set_color("FF6600").set_fill("FF0000",opacity=1).scale(0.1)
        s_label=TexMobject('S').next_to(craft,RIGHT)
        r_arrow=DoubleArrow(start=c2p(delta_x,delta_y),end=c2p(orbit_radius,delta_y))
        r_label=TexMobject('r').next_to(r_arrow,DOWN,buff=0.1)
        self.play(ReplacementTransform(sail_group,craft),FadeOut(angle_label),\
                FadeOut(angle_val),FadeIn(grid),ShowCreation(orbit),ShowCreation(sun))
        self.wait(0.5)
        self.play(FadeIn(s_label),GrowArrow(r_arrow),FadeIn(r_label))
        self.wait(0.5)
        formula=TexMobject(r'P_{0}=3.8 \times 10^{26}W \\ \
                            P=\frac{P_{0}S}{4 \pi r^{2}} \\ \
                            F=\frac{P_{0}S}{2c \pi r^{2}}').to_edge(RIGHT)
        brace=Brace(formula,UP,buff = SMALL_BUFF)
        detail=TextMobject('Total energy output of Sun each second').scale(0.55).next_to(brace,UP)
        formula_group=VGroup(formula,brace,detail)
        self.play(Write(formula_group),run_time=2.5)
        self.wait(0.5)
        rotate_angle=ValueTracker(0)
        cur_angle=[0]

        def craft_conf(obj):
            ang=rotate_angle.get_value()
            obj.move_to(c2p(*build_orbit(ang)))
            obj.rotate(ang-cur_angle[0])
            cur_angle[0]=ang
        
        craft.add_updater(craft_conf)
        txt_group=VGroup(s_label,r_arrow,r_label)
        self.play(FadeOut(txt_group))
        self.wait(0.5)
        self.play(Flash(sun,color="FFFF00",flash_radius=2.15,line_length=2),ApplyMethod(rotate_angle.set_value,2*PI),run_time=2)
        self.wait(0.1)
        self.play(Flash(sun,color="FFFF00",flash_radius=2.15,line_length=2),ApplyMethod(rotate_angle.set_value,0),run_time=2)
        self.wait(0.5)
        self.play(*[FadeOut(obj) for obj in [sun,orbit,craft,formula_group,brace,grid]])
        
    def construct(self):
        self.picContact()
        self.showPrin()

class DemoScene(GraphScene):
    def construct(self):
        sail_sec=[
            [5.52,268741924.94,0.895806,2,0.0134,5.52], 
            [9.07,289742329.12,0.965808,3,0.0201,3.55], 
            [12.48,295803989.15,0.986013,4,0.0267,3.41], 
            [15.85,298142397.00,0.993808,5,0.0334,3.37],
            [19.20,299175822.62,0.997253,6,0.0401,3.35], 
            [22.53,299659670.91,0.998866,7,0.0468,3.33], 
            [25.87,299884236.92,0.999614,8,0.0535,3.34], 
            [29.21,299977136.76,0.999924,9,0.0602,3.33],     
            [32.54,300000000.00,1,10,0.0668,3.33], 
            [35.87,299984695.05,0.999949,11,0.0735,3.33], 
        ]

        body_min={
            '\\texttt{Mercury Orbit}':['#D4BE79',1.5,298711223.53,0.995704,3.33,60,0.4011,2.73],
            '\\texttt{Venus Orbit}':['#B26A1E',1.5,298496231.13,0.994987,5.56,100,0.6684,2.23],
            '\\texttt{Earth Orbit}':['#12235B',1.5,298382470.61,0.994608,8.36,150,1.0027,2.80],
            '\\texttt{Mars}':['#CA4A04',2,298300866.32,0.994336,12.82,230,1.5374,4.46],
        }

        body_h={
            '\\texttt{Jupiter}':['#BC763A',2,298189987.40,0.993967,0.72,778,5.2005,0.51],
            '\\texttt{Saturn}':['#DBA754',2,298168420.54,0.993895,1.33,1427,9.5388,0.60],
            '\\texttt{Uranus}':['#C4EAED',2,298155363.90,0.993851,2.67,2869,19.1778,1.34],
            '\\texttt{Neptune}':['#4B6BBE',2,298150662.08,0.993836,4.20,4504,30.107,1.52],
            '\\texttt{Pluto}':['#D5B79A',2,298148708.16,0.993829,5.50,5900,39.4385,1.30],
        }
        body3=[
            [20.50,298144090.60,0.993814,22000,147.0588,15.00],
            [1.063578,298142400.73,0.993808,10000000,66844.9198,6.37],
            [4.254313,298142397.93,0.993808,40000000,267379.6791,19.14],
        ]
        
        title=TextMobject("\\textrm{Demonstration}").set_color(BLUE).scale(1.5)
        const_table=TextMobject('\\textbf{Table of Constants in Demo}').set_color(BLUE).to_corner(UL)
        self.play(FadeInFrom(title,UP),ShowCreationThenFadeAround(title))
        self.wait(1.2)
        self.play(ReplacementTransform(title,const_table))

        constxt1=TexMobject(r'm=2 \times 10^{3}kg').to_edge(LEFT+6.5*UP)
        constxt1_label=TextMobject('Solar Sail Mass').to_edge(LEFT+6.5*UP)
        constxt2=TexMobject(r's=10^{6}km^{2}').next_to(constxt1_label,DOWN,buff=0.5)
        constxt2_label=TextMobject('Solar Sail Area').next_to(constxt1_label,DOWN,buff=0.5)
        constxt3=TexMobject(r'GM=1.3 \times 10^{20} N \cdot m^{2}/kg \\ \
                            P_{0}=3.8 \times 10^{26}W \\ \
                            c=3 \times 10^{8} m/s').scale(0.85).to_edge(RIGHT)

        craft=Rectangle(height=FRAME_HEIGHT/25,width=FRAME_WIDTH/25,color=BLUE)
        craft_label=TextMobject('Solar Sail Craft').scale(0.7).next_to(craft,DOWN)

        self.play(Write(constxt1_label))
        self.wait(0.5)
        self.play(Write(constxt2_label))
        self.wait()
        self.play(Transform(constxt1_label,constxt1),Transform(constxt2_label,constxt2),Write(constxt3))
        self.wait(1.9)
        self.play(*([FadeOutAndShiftDown(mob) for mob in [constxt1_label,constxt2_label,constxt3]]+[ReplacementTransform(const_table,craft)]))
        self.wait(0.1)
        self.play(Write(craft_label))
        self.wait(0.5)
        self.play(Uncreate(craft_label))
        self.wait(0.1)
        self.play(ApplyMethod(craft.scale,25))
        self.wait()
    
        def unit_wrapper(obj):
            def unit_updater(mob):
                mob.next_to(obj,RIGHT,buff=0.1)
            return unit_updater

        vt_conf=[ValueTracker(x) for x in [1,0.0067,0,0,0,0.6,0.21,0.00234]]
        unit_conf=[TexMobject(x) for x in ['\\times 10^{9}m','AU','m/s','c','s','min','h','yr']]
        x_m ,x_au ,v_mps ,v_c ,t_s ,t_min ,t_h ,t_yr =vt_conf
        x_m_unit ,x_au_unit ,v_mps_unit ,v_c_unit ,t_s_unit ,t_min_unit ,t_h_unit ,t_yr_unit =unit_conf
        t_label=TextMobject('\\texttt{Departure Time}').scale(0.55).to_edge(DOWN)
        v_label=TextMobject('\\texttt{Speed}').scale(0.55).to_corner(DL)
        x_label=TextMobject('\\texttt{Distance from the Sun}').scale(0.55).to_corner(DR)
        view_label=TextMobject('\\texttt{FPV}').scale(0.65).to_corner(UL)

        def set_decimal(obj,places):
            return DecimalNumber(obj.get_value(),
            show_ellipsis=False,
            num_decimal_places=places,
            include_sign=False).add_updater(lambda m: m.set_value(obj.get_value())) 
        

        t_display=set_decimal(t_s,2)
        t_s_unit.add_updater(unit_wrapper(t_display))
        t_group=VGroup(t_display,t_s_unit).scale(0.6).to_edge(DOWN)

        v_c_display=set_decimal(v_c,6)
        v_c_unit.add_updater(unit_wrapper(v_c_display))
        v_c_group=VGroup(v_c_display,v_c_unit)

        v_mps_display=set_decimal(v_mps,2)
        v_mps_unit.add_updater(unit_wrapper(v_mps_display))
        v_mps_group=VGroup(v_mps_display,v_mps_unit)

        x_m_display=set_decimal(x_m,0)
        x_m_unit.add_updater(unit_wrapper(x_m_display))
        x_m_group=VGroup(x_m_display,x_m_unit)

        x_au_display=set_decimal(x_au,4)
        x_au_unit.add_updater(unit_wrapper(x_au_display))
        x_au_group=VGroup(x_au_display,x_au_unit)

        x_group=VGroup(x_m_group,x_au_group).arrange(DOWN).scale(0.6).to_corner(DR+24*LEFT)
        v_group=VGroup(v_mps_group,v_c_group).arrange(DOWN).scale(0.6).to_corner(DL)
        
        close_coe=1e5*2.5
        away_coe=1e-5
        def body_close(obj):
            obj.scale(close_coe)
            obj.shift(LEFT*FRAME_WIDTH/2)
            return obj

        def body_away(obj):
            obj.scale(away_coe)
            obj.shift(LEFT*FRAME_WIDTH/2)
            return obj
        
        #sun=Circle(color='#FF841F').set_fill('#FF841F',opacity=1).scale(1)
        #sun_label=TextMobject('\\texttt{Sun}').to_corner(UR)
        sun_near_label=TextMobject('\\texttt{Near the Sun}').to_corner(UR)
        self.play(*([FadeIn(m) for m in [x_label,t_label,v_label,view_label,sun_near_label]]))
        self.wait(1.2)
        self.play(FadeOut(x_label),FadeIn(x_group),FadeOut(t_label),FadeIn(t_group),FadeOut(v_label),FadeIn(v_group))
        self.wait(0.5)
        '''
        self.play(*([ApplyFunction(body_away,sun,run_time=15.85,rate_func=rush_into)]+[FadeOut(sun_label,run_time=10)]\
                +[ApplyMethod(m,v,run_time=15.85) for detail in sun_sec for m,v in [(t_s.set_value,detail[0]),(v_mps.set_value,detail[1]),\
                (v_c.set_value,detail[2]),(x_m.set_value,detail[3]),(x_au.set_value,detail[4])]]))
        '''
        self.play(FadeOut(sun_near_label))
        for detail in sail_sec:
            self.play(*(ApplyMethod(m,v,run_time=detail[5]) for m,v in [(t_s.set_value,detail[0]),(v_mps.set_value,detail[1]),\
                (v_c.set_value,detail[2]),(x_m.set_value,detail[3]),(x_au.set_value,detail[4])]))
        
        ff_label=TexMobject('\\blacktriangleright \\blacktriangleright \\times 60').scale(0.65).to_corner(UL)
        t_display=set_decimal(t_min,2)
        t_min_unit.add_updater(unit_wrapper(t_display))
        t_group_min=VGroup(t_display,t_min_unit).scale(0.6).to_edge(DOWN)
        self.play(ReplacementTransform(view_label,ff_label),FadeOut(t_group),FadeIn(t_group_min),run_time=0.001)
        
        for name,contxt in body_min.items():
            body_circle=Circle(color=contxt[0]).to_edge(RIGHT).set_fill(contxt[0],opacity=1).scale(away_coe)
            body_label=TextMobject(name).to_corner(UR)
            close_coe=1e5*contxt[1]
            self.play(*(ApplyMethod(m,v,run_time=contxt[7]) for m,v in [(t_min.set_value,contxt[4]),(v_mps.set_value,contxt[2]),\
                (v_c.set_value,contxt[3]),(x_m.set_value,contxt[5]),(x_au.set_value,contxt[6])]))
            self.play(FadeIn(body_label),ApplyFunction(body_close,body_circle),run_time=0.2,rate_func=linear)
            self.wait(0.5)
            self.play(FadeOut(body_label),ApplyFunction(body_away,body_circle),run_time=0.2,rate_func=linear)

        ff_label_1=TexMobject('\\blacktriangleright \\blacktriangleright \\times 3600').scale(0.65).to_corner(UL)
        t_display=set_decimal(t_h,2)
        t_h_unit.add_updater(unit_wrapper(t_display))
        t_group_h=VGroup(t_display,t_h_unit).scale(0.6).to_edge(DOWN)
        self.play(ReplacementTransform(ff_label,ff_label_1),FadeOut(t_group_min),FadeIn(t_group_h),run_time=0.001)
        
        for name,contxt in body_h.items():
            body_circle=Circle(color=contxt[0]).to_edge(RIGHT).set_fill(contxt[0],opacity=1).scale(away_coe)
            body_label=TextMobject(name).to_corner(UR)
            close_coe=1e5*contxt[1]
            self.play(*(ApplyMethod(m,v,run_time=contxt[7]) for m,v in [(t_h.set_value,contxt[4]),(v_mps.set_value,contxt[2]),\
                (v_c.set_value,contxt[3]),(x_m.set_value,contxt[5]),(x_au.set_value,contxt[6])]))
            self.play(FadeIn(body_label),ApplyFunction(body_close,body_circle),run_time=0.19,rate_func=linear)
            self.wait(0.5)
            self.play(FadeOut(body_label),ApplyFunction(body_away,body_circle),run_time=0.19,rate_func=linear)
        
        voyager_dot=SmallDot().set_color('#5B584F')
        voyager_label=TextMobject('\\textsc{Voyager 1}').scale(1.25).next_to(voyager_dot,DOWN)
        voyager_group=VGroup(voyager_dot,voyager_label).to_edge(RIGHT)
        vcontxt=body3[0]
        self.play(*(ApplyMethod(m,v,run_time=vcontxt[5]) for m,v in [(t_h.set_value,vcontxt[0]),(v_mps.set_value,vcontxt[1]),\
                (v_c.set_value,vcontxt[2]),(x_m.set_value,vcontxt[3]),(x_au.set_value,vcontxt[4])]))
        self.play(ApplyMethod(voyager_group.shift,LEFT*FRAME_WIDTH/2),run_time=0.19,rate_func=linear)
        self.wait(0.5)
        self.play(ApplyMethod(voyager_group.shift,LEFT*FRAME_WIDTH/2),run_time=0.19,rate_func=linear)

        ff_label_2=TexMobject('\\blacktriangleright \\blacktriangleright \\times 5,256,000').scale(0.65).to_corner(UL)
        t_display=set_decimal(t_yr,6)
        t_yr_unit.add_updater(unit_wrapper(t_display))
        t_group_yr=VGroup(t_display,t_yr_unit).scale(0.6).to_edge(DOWN)
        self.play(ReplacementTransform(ff_label_1,ff_label_2),FadeOut(t_group_h),FadeIn(t_group_yr),run_time=0.001)

        oly_label=TextMobject('\\texttt{One Light Year}').to_corner(UR)
        lycontxt=body3[1]
        self.play(*(ApplyMethod(m,v,run_time=lycontxt[5]) for m,v in [(t_yr.set_value,lycontxt[0]),(v_mps.set_value,lycontxt[1]),\
                (v_c.set_value,lycontxt[2]),(x_m.set_value,lycontxt[3]),(x_au.set_value,lycontxt[4])]))
        self.play(FadeIn(oly_label),run_time=0.001)
        self.wait(0.5)
        self.play(FadeOut(oly_label),run_time=0.001)

        centauri_circle=Circle(color='#FAFCF7').to_edge(RIGHT).set_fill('#FAFCF7',opacity=1).scale(away_coe)
        centauri_label=TextMobject('\\texttt{Proxima Centauri}').to_corner(UR)
        close_coe=1e5*2
        pcontxt=body3[2]
        self.play(*(ApplyMethod(m,v,run_time=pcontxt[5]) for m,v in [(t_yr.set_value,pcontxt[0]),(v_mps.set_value,pcontxt[1]),\
                (v_c.set_value,pcontxt[2]),(x_m.set_value,pcontxt[3]),(x_au.set_value,pcontxt[4])]))
        self.play(FadeIn(centauri_label),ApplyFunction(body_close,centauri_circle),run_time=0.12,rate_func=linear)
        self.wait(0.5)
        self.play(FadeOut(centauri_label),ApplyFunction(body_away,centauri_circle),run_time=0.12,rate_func=linear)
        self.wait(0.1)
        self.play(*([FadeOutAndShift(x,y) for x,y in [(ff_label_2,UP),(t_group_yr,DOWN),(x_group,DOWN),(v_group,DOWN)]]+[FadeOut(craft)]))
        self.wait()