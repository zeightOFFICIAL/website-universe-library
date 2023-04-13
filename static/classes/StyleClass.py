class Style:
    def ReturnBorderImage(first_color, second_color):
        return f'border-image: linear-gradient(to right,{first_color},{second_color}) 1;'
    def ReturnBoxShadow(color):
        return f'box-shadow: 0 0 20px {color};'
    def ReturnPStyle():
        return f'text-align: center; font-family: \'normal\'; font-size: 3vmin; cursor: default; color: #fff'
    def ReturnFilling(first_color, second_color):
        return f'background-color: {first_color}; background-image: linear-gradient(to right, {first_color}, {second_color})'
    def ReturnImageScalePanel():
        return 'style="width: 100%; height: 35vmin; object-fit: cover;"'