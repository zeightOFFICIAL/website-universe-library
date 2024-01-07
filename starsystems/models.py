from django.db import models


class ObjectTypes(models.Model):
    type_name = models.TextField(db_column='type_NAME')  

    class Meta:
        managed = False
        db_table = 'object_types'


class Objects(models.Model):
    div_id_name = models.TextField(db_column='div_id_NAME')  
    system = models.ForeignKey('Systems', models.DO_NOTHING, db_column='system_ID', blank=True, null=True)  
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_ID', blank=True, null=True)  
    name_name = models.TextField(db_column='name_NAME')  
    type = models.ForeignKey(ObjectTypes, models.DO_NOTHING, db_column='type_ID')  
    size_int = models.IntegerField(db_column='size_INT')  
    prime_color_any = models.TextField(db_column='prime_color_ANY')  
    second_color_any = models.TextField(db_column='second_color_ANY')  
    shadow_color_any = models.TextField(db_column='shadow_color_ANY')  
    shadow_power_int_px = models.IntegerField(db_column='shadow_power_INT_PX')  
    orbit_size_int_vmin = models.IntegerField(db_column='orbit_size_INT_VMIN')  
    orbit_time_int_s = models.IntegerField(db_column='orbit_time_INT_S')  

    class Meta:
        managed = False
        db_table = 'objects'


class PanelTypes(models.Model):
    name_name = models.TextField(db_column='name_NAME')  
    args_len_int = models.IntegerField(db_column='args_len_INT')  

    class Meta:
        managed = False
        db_table = 'panel_types'


class Panels(models.Model):
    div_id_name = models.TextField(db_column='div_id_NAME')  
    type = models.ForeignKey(PanelTypes, models.DO_NOTHING, db_column='type_ID')  
    values = models.ForeignKey('ValueRow', models.DO_NOTHING, db_column='values_ID')  
    parent_object = models.ForeignKey(Objects, models.DO_NOTHING, db_column='parent_object_ID', blank=True, null=True)  
    parent_system = models.ForeignKey('Systems', models.DO_NOTHING, db_column='parent_system_ID', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'panels'


class Systems(models.Model):
    name_name = models.TextField(db_column='name_NAME')  
    prime_color_any = models.TextField(db_column='prime_color_ANY', blank=True, null=True)  
    second_color_any = models.TextField(db_column='second_color_ANY', blank=True, null=True)  
    shadow_color_any = models.TextField(db_column='shadow_color_ANY', blank=True, null=True)  
    univ_thumbnail_text_url = models.TextField(db_column='univ_thumbnail_TEXT_URL', blank=True, null=True)  
    icon_path_text_url = models.TextField(db_column='icon_path_TEXT_URL', blank=True, null=True)  
    short_desc_text = models.TextField(db_column='short_desc_TEXT', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'systems'


class ValueRow(models.Model):
    title_plain = models.TextField(db_column='title_PLAIN', blank=True, null=True)  
    text_plain = models.TextField(db_column='text_PLAIN', blank=True, null=True)  
    img_src_plain = models.TextField(db_column='img_src_PLAIN', blank=True, null=True)  
    color_a_plain = models.TextField(db_column='color_a_PLAIN', blank=True, null=True)  
    color_b_plain = models.TextField(db_column='color_b_PLAIN', blank=True, null=True)  
    color_c_plain = models.TextField(db_column='color_c_PLAIN', blank=True, null=True)  
    is_slider_bool = models.TextField(db_column='is_slider_BOOL', blank=True, null=True)  
    h_color_a_plain = models.TextField(db_column='h_color_a_PLAIN', blank=True, null=True)  
    h_color_b_plain = models.TextField(db_column='h_color_b_PLAIN', blank=True, null=True)  
    h_color_c_plain = models.TextField(db_column='h_color_c_PLAIN', blank=True, null=True)  
    close_button_bool = models.TextField(db_column='close_button_BOOL', blank=True, null=True)  
    extra_args = models.TextField(db_column='extra_ARGS', blank=True, null=True)  
    layout_int = models.IntegerField(db_column='layout_INT')  

    class Meta:
        managed = False
        db_table = 'value_row'