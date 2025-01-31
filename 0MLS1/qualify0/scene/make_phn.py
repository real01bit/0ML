import json

template = '''
Scene.addCircle {
    _id := "%s";
    _nameflag := false;
    collideSet := 1;
    drawBorder := false;
    color := [%lf,%lf,%lf,1];
    drawCake := false;
    onDie := (e)=>{};
    radius := 0.25000000;
    pos := [%lf,%lf];
    materialName := "%s";
    onSpawn := (e)=>{
        _nameflag ? {} : {
            Scene.addBox {
                _follow := e.this.entityID;
                text := "%s";
                textFont := "DIN Pro";
                textFontSize := 128;
                textScale := 0.5;
                size := [2,0.5];
                color := [0,0,0,0];
                drawBorder := false;
                density := +inf;
                pos := {
                    ent = scene.entityByID(_follow);
                    ent.pos + [0,0.5]
                };
                collideSet := 0;
            };
            _nameflag = true;
        };
    };
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
              color[2], pos[0], pos[1], marble['name'], marble['name']))
    i += 1
