import random

class Style:
    class Box:
        @staticmethod
        def text_info(a_color, b_color, c_color, slider=False):
            if slider == True:
                return ""
            border = f'border-width:3px;border-style:solid;margin:40px 15px;border-image:linear-gradient(to right,{a_color},{b_color}) 1;'
            shadow = f'box-shadow:0 0 20px {c_color};'
            return f'style="{border+shadow}"'

        @staticmethod
        def slider_info(a_color, b_color, c_color):
            border = f'border-width:3px;border-style:solid;margin:40px 15px;border-image:linear-gradient(to right,{a_color},{b_color}) 1;'
            shadow = f'box-shadow:0 0 20px {c_color};'
            overflow = f'overflow:hidden;'
            return f'style="{border+shadow+overflow}"'

        @staticmethod
        def image_info(a_color, b_color, c_color, slider=False):
            if slider == True:
                return ""
            border = f'border-width:3px;border-style:solid;margin:40px 15px;border-image:linear-gradient(to right,{a_color},{b_color}) 1;'
            shadow = f'box-shadow:0 0 20px {c_color};'
            filling = f'background-color:{a_color};background-image:linear-gradient(to right, {a_color}, {b_color});'
            return f'style="{border+shadow+filling}"'

    class Text:
        @staticmethod
        def normal():
            style = f'text-align:center;font-family:\'normal\';font-size:3vmin;cursor:default;color:#fff;padding-left:20px;padding-right:20px;'
            return f'style="{style}"'

        @staticmethod
        def header_one(a_color, b_color):
            style = f'text-align:center;font-family:\'solar\';font-size:7vmin;margin-bottom:2.5vmin;cursor:default;padding-left:20px;padding-right:20px;'
            font = f'background-color:{a_color};background-image:linear-gradient(62deg, {a_color} 0%, {b_color} 100%);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
            return f'style="{style+font}"'

        @staticmethod
        def header_two(a_color, b_color):
            style = f'text-align:center;font-family:\'solar\';font-size:5.5vmin;margin-bottom:2.5vmin;cursor:default;padding-left:20px;padding-right:20px;'
            font = f'background-color:{a_color};background-image:linear-gradient(62deg, {a_color} 0%, {b_color} 100%);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent;'
            return f'style="{style+font}"'
        
        @staticmethod
        def sidepanel():
            style = f"display:block;color:#aaa;cursor:pointer;overflow-x:hidden;overflow-y:hidden;white-space:nowrap;"
            font =  f"font-family:'side';font-size:3.5vmin;font-weight:900;"
            size =  f"padding-bottom:1vmin;padding-left:15%;height:4vmin;"
            animation = f'transition:.15s;'
            return f'style="{style+font+size+animation}"'
            

    class Image:
        @staticmethod
        def default():
            style = f'width:100%;height:45vmin;object-fit:cover;'
            return f'style="{style}"'

        @staticmethod
        def original():
            style = f'width:100%;object-fit:cover;'
            return f'style="{style}"'

    class Video:
        @staticmethod
        def normal():
            arg = f'id="video" width="100%" height="315"'
            specifics = f'title="" frameborder="0" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture"'
            return f'{arg+specifics} allowfullscreen'

    class Misc:
        @staticmethod
        def overflow_hidden():
            return f'style="overflow:hidden;"'

        @staticmethod
        def accent_bar(a_color, b_color):
            sizes = f'top:0;left:0;width:10vmin;height:100vh;'
            animations = f'transition:left .7s;transition:right .7s;'
            position = f'position:absolute;'
            color = f'background-color:{a_color};background-image:linear-gradient(62deg, {a_color} 0%, {b_color} 100%);box-shadow:0 0 3vw {a_color};'
            return f'style="{sizes+animations+position+color}"'

    class Button:
        @staticmethod
        def slider_left(a_color):
            interactive = f'display:inline;color:#000;cursor:pointer;transition:.5s;background:transparent;border:none;'
            text = f'font-size:2vmin;background-color:{a_color};margin:0;padding:0;overflow:hidden;'
            position = f'float:left;width:50%;'
            return f'style="{interactive+text+position}"'

        @staticmethod
        def slider_right(a_color):
            interactive = f'display:inline;color:#000;cursor:pointer;transition:.5s;background:transparent;border:none;'
            text = f'font-size:2vmin;background-color:{a_color};margin:0;padding:0;overflow:hidden;'
            position = f'float:right;width:50%;'
            return f'style="{interactive+text+position}"'


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
            lumin = f'box-shadow 0 0 {self.lumin} {self.c_color};'
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
    class SlidesButton:
        def __init__(self, args, slider_name):
            self.args = args
            self.name = slider_name

        def __str__(self):
            return f'onclick="plusSlides({self.args},{self.name});"'