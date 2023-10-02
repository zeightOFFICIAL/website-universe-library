from django.db import models


class ObjectTypes(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = "object_types"


class Objects(models.Model):
    div_id = models.TextField()
    system = models.ForeignKey("Systems", models.DO_NOTHING)
    parent = models.ForeignKey("self", models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    type_name = models.ForeignKey(ObjectTypes, models.DO_NOTHING, db_column="typename")
    size = models.IntegerField()
    prime_color = models.TextField()
    second_color = models.TextField()
    shadow_color = models.TextField()
    shadow_power = models.IntegerField()
    orbit_size = models.IntegerField()
    orbit_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = "objects"


class PanelTypes(models.Model):
    name = models.TextField(unique=True)
    value_length = models.IntegerField()

    class Meta:
        managed = False
        db_table = "panel_types"


class Panels(models.Model):
    div_id = models.TextField()
    type = models.ForeignKey(PanelTypes, models.DO_NOTHING)
    values = models.ForeignKey("ValueRow", models.DO_NOTHING)
    parent_object = models.ForeignKey("Objects", models.DO_NOTHING)
    parent_system = models.ForeignKey("Systems", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "panels"


class Systems(models.Model):
    name = models.TextField(unique=True)
    icon_path = models.TextField(blank=True, null=True)
    prime_color = models.TextField(blank=True, null=True)
    second_color = models.TextField(blank=True, null=True)
    shadow_color = models.TextField(blank=True, null=True)
    univ_thumbnail = models.TextField(blank=True, null=True)
    large_cover = models.TextField(blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "systems"


class ValueRow(models.Model):
    title = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    img_src = models.TextField(blank=True, null=True)
    color_a = models.TextField(blank=True, null=True)
    color_b = models.TextField(blank=True, null=True)
    color_c = models.TextField(blank=True, null=True)
    is_slider = models.TextField(blank=True, null=True)
    h_color_a = models.TextField(blank=True, null=True)
    h_color_b = models.TextField(blank=True, null=True)
    h_color_c = models.TextField(blank=True, null=True)
    close_button = models.TextField(blank=True, null=True)
    extra_hrefs = models.TextField(blank=True, null=True)
    layout = models.IntegerField()

    class Meta:
        managed = False
        db_table = "value_row"
