class Style:
    class Box:
        def ReturnText(a_color, b_color, c_color, slider = False):
            if slider == True: return ""            
            part =     f'border-width: 3px; border-style: solid; margin: 40px 15px;'
            part_one = f'border-image: linear-gradient(to right,{a_color},{b_color}) 1;'
            part_two = f'box-shadow: 0 0 20px {c_color};'
            return f'style="{part+part_one+part_two}"'
        def ReturnSliderText(a_color, b_color, c_color):
            part =     f'border-width: 3px; border-style: solid; margin: 40px 15px;'
            part_one = f'border-image: linear-gradient(to right,{a_color},{b_color}) 1;'
            part_two = f'box-shadow: 0 0 20px {c_color};'
            part_thr = f'overflow: hidden;'
            return f'style="{part+part_one+part_two+part_thr}"'
        def ReturnImage(a_color, b_color, c_color, slider = False):
            if slider == True: return ""      
            part =     f'border-width: 3px; border-style: solid; margin: 40px 15px;'
            part_one = f'border-image: linear-gradient(to right,{a_color},{b_color}) 1;'
            part_two = f'box-shadow: 0 0 20px {c_color};'
            part_thr = f'background-color: {a_color};background-image: linear-gradient(to right, {a_color}, {b_color});'
            return f'style="{part+part_one+part_two+part_thr}"'
    class Text:
        def ReturnNormal():
            part = f'text-align: center;font-family: \'normal\';font-size: 3vmin; cursor: default; color: #fff;padding-left: 20px; padding-right: 20px;'
            return f'style="{part}"'
        def ReturnHeader(a_color, b_color):
            part =     f'text-align: center;font-family: \'solar\';font-size: 7vmin;margin-bottom: 2.5vmin;cursor: default;padding-left: 20px; padding-right: 20px;'
            part_one = f'background-color: {a_color};background-image: linear-gradient(62deg, {a_color} 0%, {b_color} 100%);background-clip: text;-webkit-background-clip: text;-webkit-text-fill-color: transparent;'
            return f'style="{part+part_one}"'
        def ReturnTitle(a_color, b_color):
            part =     f'text-align: center;font-family: \'solar\';font-size: 5.5vmin;margin-bottom: 2.5vmin;cursor: default;padding-left: 20px; padding-right: 20px;'
            part_one = f'background-color: {a_color};background-image: linear-gradient(62deg, {a_color} 0%, {b_color} 100%);background-clip: text;-webkit-background-clip: text;-webkit-text-fill-color: transparent;'
            return f'style="{part+part_one}"'
    class Image:
        def ReturnImage():
            part = f'width: 100%;height: 45vmin;object-fit: cover;'
            return f'style="{part}"'
        def ReturnImageOriginal():
            part = f'width: 100%;object-fit: cover;'
            return f'style="{part}"'
    class Video:
        def ReturnVideo():
            part =     f'id="video" width="100%" height="315"'
            part_two = f'title="" frameborder="0"'
            part_thr = f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"'
            return f'{part+part_two+part_thr} allowfullscreen'
    class Misc:
        def ReturnHidden():
            return f'style="overflow: hidden;"'
        def ReturnAccentBar(fore_color, back_color):
            sizes = f'top:0;left:0;width:10vmin;height:100vh;'
            animations = f'transition:left .7s; transition:right .7s;'
            position = f'position:absolute;'
            color = f'background-color:{fore_color};background-image: linear-gradient(62deg, {fore_color} 0%, {back_color} 100%);box-shadow: 0 0 3vw {fore_color};'
            return f'style="{sizes+animations+position+color}"'               
    class Button:
        def ReturnSliderLeft(fore_color):
            part     = f'display: inline;color: #000;cursor: pointer;transition: .5s;background: transparent;border: none;'
            part_one = f'font-size: 2vmin;background-color: {fore_color};margin: 0;padding: 0;overflow: hidden;'
            part_two = f'float: left;width: 50%;'
            return f'style="{part+part_one+part_two}"'
        def ReturnSliderRight(fore_color):
            part     = f'display: inline;color: #000;cursor: pointer;transition: .5s;background: transparent;border: none;'
            part_one = f'font-size: 2vmin;background-color: {fore_color};margin: 0;padding: 0;overflow: hidden;'
            part_two = f'float: right;width: 50%;'
            return f'style="{part+part_one+part_two}"'

class Visual:
    class Object:
        def __init__(self, size, margins, first_color, second_color, lumin):
            self.size = size
            self.margins = margins
            self.first_color = first_color
            self.second_color = second_color
            self.lumin = lumin
        def __str__(self):
            size = f'height: {self.size};width: {self.size};'
            margins = f'margin-top: {self.margins}; margin-left: {self.margins};'
            fill = f'background: {self.first_color}; background: radial-gradient(circle, {self.first_color} 0%, {self.second_color} 100%);'
            return f'style="{size+margins+fill}"'
    class Orbit:
        def __init__(self, width, height, margin_top, margin_left):
            self.width = width
            self.height = height
            self.margin_top = margin_top
            self.margin_left = margin_left
        def __str__(self):
            size = f'width:{self.width};height:{self.height};margin-top:{self.margin_top};margin-left:{self.margin_left};'
            return f'class="orbit" style="{size}"'            
    class Spin:
        def __init__(self, width, height, margin_top, margin_left, period, radius):
            self.width = width
            self.height = height
            self.margin_top = margin_top
            self.margin_left = margin_left
            self.period = period
            self.radius = radius
        def __str__(self):
            size = f'width:{self.width};height:{self.height};'
            margins = f'margin-top:{self.margin_top};margin-left:{self.margin_left};'
            animation = f'animation: spin-right {self.period} linear infinite; border-radius: {self.radius};'
            return f'style="{size+margins+animation}"'

class EventHandlers:
    class SlidesButton:
        def __init__(self, args, slide_name):
            self.args = args
            self.slide_name = slide_name
        def __str__(self):
            return f'onclick="plusSlides({self.args},{self.slide_name});"'