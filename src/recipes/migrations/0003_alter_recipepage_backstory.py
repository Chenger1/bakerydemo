# Generated by Django 4.2.4 on 2023-08-18 08:16

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipepage_backstory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepage',
            name='backstory',
            field=wagtail.fields.StreamField([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False))])), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('attribute_name', wagtail.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', icon='media', template='blocks/embed_block.html'))], blank=True, help_text='Use only a minimum number of headings and large blocks.', use_json_field=True),
        ),
    ]
