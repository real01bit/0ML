import json

template = '''
Scene.addCircle {
    _id := "%s";
    collideSet := 1;
    drawBorder := false;
    color := [%lf,%lf,%lf,1];
    drawCake := false;
    onDie := (e)=>{};
    radius := 0.25000000;
    pos := [%lf,%lf];
    materialName := "%s";
};
'''

phn = open('layout.phn', 'w', encoding='utf-8')
with open('../data/marble.json', 'r') as fp:
    marbles = json.loads(fp.read())
i = 0
for id in marbles.keys():
    marble = marbles[id]
    color = (marble['color'][0]/255,
             marble['color'][1]/255, marble['color'][2]/255)
    pos = ((i % 10) * 0.5, -(i // 10) * 0.5)
    phn.write(template % (id, color[0], color[1],
              color[2], pos[0], pos[1], marble['name']))
    i += 1
