import random


class Style:
    class Box:
        @staticmethod
        def text_info(a_color, b_color, c_color, slider=False):
            if slider == True:
                return "style=\"display:none;\" class=\"Slider\""
            style = f'display:block;border-width:3px;border-style:solid;margin:40px 15px;border-image:linear-gradient(to right,{a_color},{b_color}) 1;box-shadow:0 0 20px {c_color};border-color:{a_color};transition:box-shadow 1.1s,border-color 1.1s,border-image 1.1s;'
            return f'style="{style}"'

        @staticmethod
        def slider_info(a_color, b_color, c_color):
            style = f'border-width:3px;border-style:solid;margin:40px 15px;border-image:linear-gradient(to right,{a_color},{b_color}) 1;box-shadow:0 0 20px {c_color};overflow:hidden;border-color:{a_color};transition:box-shadow 1.1s,border-color 1.1s,border-image 1.1s;'
            return f'style="{style}"'

        @staticmethod
        def image_info(a_color, b_color, c_color, slider=False):
            if slider == True:
                return f"style=\"display:none;background-color:{a_color};background-image:linear-gradient(to right, {a_color}, {b_color});\" class=\"Slider\""
            style = f'display:block;border-width:3px;border-style:solid;margin:40px 15px;border-image:linear-gradient(to right,{a_color},{b_color}) 1;box-shadow:0 0 20px {c_color};background-color:{a_color};background-image:linear-gradient(to right, {a_color}, {b_color});border-color:{a_color};transition:box-shadow 1.1s,border-color 1.1s,border-image 1.1s,background-color 1.1s'
            return f'style="{style}"'

    class Text:
        @staticmethod
        def normal():
            style = f'text-align:center;font-family:\'normal\';font-size:3vmin;cursor:default;color:#fff;padding-left:20px;padding-right:20px;'
            return f'style="{style}"'

        @staticmethod
        def header_one(a_color, b_color):
            style = f'text-align:center;font-family:\'solar\';font-size:7vmin;margin-bottom:2.5vmin;cursor:default;padding-left:2vmin;padding-right:2vmin;background-color:{a_color};background-image:linear-gradient(62deg, {a_color} 0%, {b_color} 100%);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
            return f'style="{style}"'

        @staticmethod
        def header_two(a_color, b_color):
            style = f'text-align:center;font-family:\'solar\';font-size:5.5vmin;margin-bottom:2.5vmin;cursor:default;padding-left:2vmin;padding-right:2vmin;background-color:{a_color};background-image:linear-gradient(62deg, {a_color} 0%, {b_color} 100%);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
            return f'style="{style}"'

        @staticmethod
        def sidepanel():
            style = f'min-width:100vh;width:100vh;display:block;color:#aaa;cursor:pointer;overflow-x:hidden;overflow-y:hidden;white-space:nowrap;font-family:\'side\';font-size:3.5vmin;padding-bottom:1vmin;height:4vmin;transition:.3s;font-weight:bolder;'
            return f'style="{style}"'

    class Image:
        @staticmethod
        def default():
            style = f'width:100%;height:45vmin;object-fit:cover;'
            return f'style="{style}"'

        @staticmethod
        def original():
            style = f'width:100%;object-fit:cover;'
            return f'style="{style}"'

        @staticmethod
        def short(position):
            style = f'position:absolute;left:120%;height:20vmin;transition:.5s;top:{position}'
            return f'style="{style}"'

    class Video:
        @staticmethod
        def normal():
            args = f'width="100%"height="315"title=""frameborder="0"allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture"'
            return f'{args} allowfullscreen'

    class Misc:
        @staticmethod
        def overflow_hidden():
            return f'style="overflow:hidden;"'

        @staticmethod
        def accent_bar(a_color, b_color):
            style = f'top:0;left:0;width:5%;height:100vh;transition:left .7s,right .7s;position:absolute;background-color:{a_color};background-image:linear-gradient(62deg, {a_color} 0%, {b_color} 100%);box-shadow:0 0 3vw {a_color};'
            return f'style="{style}"'

        @staticmethod
        def sidepanel_univ_href(extra_directives=""):
            style = f'text-align:center;font-family:\'solar\';font-size:4vmin;font-weight:bolder;display:block;overflow:hidden;padding:1.5vmin 0; height:7vmin;cursor:block;transition:.5s;-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
            return f'style="{style+extra_directives}"'

    class Button:
        @staticmethod
        def slider_left(a_color):
            style = f'display:inline;color:#000;cursor:pointer;transition:.5s;background:transparent;border:none;font-size:2vmin;background-color:{a_color};margin:0;padding:0.5vmin 0;overflow:hidden;float:left;width:50%;'
            return f'style="{style}"'

        @staticmethod
        def slider_right(a_color):
            style = f'display:inline;color:#000;cursor:pointer;transition:.5s;background:transparent;border:none;font-size:2vmin;background-color:{a_color};margin:0;padding:0.5vmin 0;overflow:hidden;float:right;width:50%;'
            return f'style="{style}"'

        @staticmethod
        def close_sidepanel(color, position="0"):
            style = f'font-family:\'solar\';font-size:3vmin;font-weight:bolder;text-decoration:none;color:#000;position:absolute;top:{position};left:0;border:none;padding:2vmin 0;cursor:pointer;width:16vh;overflow:hidden;text-align:left;background:{color};box-shadow:{color} 0px 0px 70px;transition:.5s;padding-left:1.8vmax;min-width:60vh;'
            return f'style="{style}"'

        @staticmethod
        def open_sidepanel(position="0"):
            style = f'font-family:\'solar\';font-size:3vmin;font-weight:bolder;text-decoration:none;color:#000;position:absolute;top:{position};left:0;z-index:1;border:none;padding:2vmin 0;cursor:pointer;background-color:rgba(255,255,255,0);transition:background.5s, box-shadow.5s;overflow:hidden;padding-left:1.8%;width:3.2%;'
            return f'style="{style}"'

        @staticmethod
        def on_border(a_color, b_color, y=30, x="5.5%"):
            style = f'position:absolute;top:{y}px;padding:0 1.2vmax;text-align:center;border:solid 2px #000;font-size:3vmin;cursor:pointer;background-color:{a_color};background-image:linear-gradient(62deg, {a_color} 0%, {b_color} 100%);left:{x};text-decoration:none;color:#000;'
            return f'style="{style}"'


class Visual:
    class Object:
        def __init__(self, args, z_index):
            self.size = args[0]
            self.margins = args[1]
            self.a_color = args[2]
            self.b_color = args[3]
            self.lumin = args[4]
            self.z_index = z_index
            self.c_color = self.b_color if len(args) < 6 else args[5]

        def __str__(self):
            size = f'height:{self.size};width:{self.size};'
            margins = f'margin-top:{self.margins};margin-left:{self.margins};'
            fill = f'background:{self.a_color};background:radial-gradient(circle, {self.a_color} 0%, {self.b_color} 100%);cursor:pointer;'
            lumin = f'box-shadow: 0 0 {self.lumin} {self.c_color};'
            zindex = f'z-index:{self.z_index};' if self.z_index != -998 else ""
            return f'style="{size+margins+fill+lumin+zindex}"'

    class Orbit:
        def __init__(self, args):
            self.size = args[0]
            self.margins = args[1]

        def __str__(self):
            size = f'width:{self.size};height:{self.size};margin-top:{self.margins};margin-left:{self.margins};'
            return f'class="orbit" style="{size}"'

    class Spin:
        def __init__(self, args, z_index):
            self.size = args[0]
            self.margins = args[1]
            self.period = args[2]
            self.z_index = z_index

        def __str__(self):
            size = f'width:{self.size};height:{self.size};'
            margins = f'margin-top:{self.margins};margin-left:{self.margins};'
            animation = f'animation:spin-right {self.period}s linear infinite;border-radius:100%;'
            shift = random.randint(0, int(self.period))
            animation_random = f'animation-delay:-{shift}s'
            return f'style="{size+margins+animation+animation_random};z-index:{self.z_index};"'


class EventHandlers:
    @staticmethod
    def slider_click(arg, slider_name):
        call = f'onclick="plusSlides({arg},\'{slider_name}\');"'
        return call

    @staticmethod
    def object_click(id):
        call = f'onclick="objClicked(\'{id}\');closeSidepanel();"'
        return call

    @staticmethod
    def hover(id, class_name):
        call = f'onmouseover="onHoverEnterAddClass(\'{id}\',\'{class_name}\');" onmouseout="onHoverLeaveRemoveClass(\'{id}\',\'{class_name}\');"'
        return call

    @staticmethod
    def hover_2d(id, id2, class_name, class_name2):
        call = f'onmouseover="onHoverEnterAddClass(\'{id}\',\'{class_name}\');onHoverEnterAddClass(\'{id2}\',\'{class_name2}\');" onmouseout="onHoverLeaveRemoveClass(\'{id}\',\'{class_name}\');onHoverLeaveRemoveClass(\'{id2}\',\'{class_name2}\');"'
        return call

    @staticmethod
    def hover_side_name(id, color):
        call = f'onmouseover="onHoverSidepanelTitle(\'{id}\',\'{color}\');" onmouseout="onHoverSidepanelTitleLeave(\'{id}\',\'{color}\');"'
        return call
