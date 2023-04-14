class Style:
    class Box:
        def ReturnText(a_color, b_color, c_color):
            part =     f'border-width: 3px; border-style: solid; margin: 40px 15px;'
            part_one = f'border-image: linear-gradient(to right,{a_color},{b_color}) 1;'
            part_two = f'box-shadow: 0 0 20px {c_color};'
            return f'style="{part+part_one+part_two}"'
        def ReturnImage(a_color, b_color, c_color):
            part =     f'border-width: 3px; border-style: solid; margin: 40px 15px;'
            part_one = f'border-image: linear-gradient(to right,{a_color},{b_color}) 1;'
            part_two = f'box-shadow: 0 0 20px {c_color};'
            part_thr =f'background-color: {a_color};background-image: linear-gradient(to right, {a_color}, {b_color});'
            return f'style="{part+part_one+part_two+part_thr}"'
    class Text:
        def ReturnNormal():
            part = f'text-align: center;font-family: \'normal\';font-size: 3vmin; cursor: default; color: #fff;'
            return f'style="{part}"'
        def ReturnHeader(a_color, b_color):
            part =     f'text-align: center;font-family: \'solar\';font-size: 7vmin;margin-bottom: 2.5vmin;cursor: default;'
            part_one = f'background-color: #FBAB7E;background-image: linear-gradient(62deg, {a_color} 0%, {b_color} 100%);background-clip: text;-webkit-background-clip: text;-webkit-text-fill-color: transparent;'
            return f'style="{part+part_one}"'
    class Image:
        def ReturnImage():
            part = f'width: 100%;height: 45vmin;object-fit: cover;'
            return f'style="{part}"'
    class Video:
        def ReturnVideo():
            part =     f'id="video" width="100%" height="315"'
            part_two = f'title="" frameborder="0"'
            part_thr = f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"'
            return f'{part+part_two+part_thr} allowfullscreen'