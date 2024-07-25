import json
with open('../marble/marble_list.json', 'r', encoding='utf-8') as fp:
    colors = json.loads(fp.read())
dot = '\u25cf'
div = '<span style=\"color:white;\">\u3001</span>'
texts = []
for id in colors.keys():
    if colors[id]['basic']:
        continue
    text = '<span style=\"color:%s;\">%s</span><span style=\"color:white;\">%s</span>' % (
        colors[id]['hex'], dot, colors[id]['name'])
    texts.append(text)
html = '''
<style>
    @font-face{
        font-family:adobe;
        src:url(\"file:///C:/Users/DELL/AppData/Local/Microsoft/Windows/Fonts/SourceHanSerifSC-Regular.otf\");
    }
    #global{
        font-family:adobe;
    }
</style>
<span id=\"global\">%s</span>''' % (
    div.join(texts[70:121]))
with open('text.html', 'w', encoding='utf-8') as fp:
    fp.write(html)
