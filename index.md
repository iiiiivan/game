<link rel="stylesheet" type="text/css" media="all" href="style.css" />

# Game
by Ivan

![game](vid_small.gif)

---

## Code

### The Enemy Class

``` python
class Enemy(Sprite):
    
    def on_create(self):
        self.scale=30
        self.goto_random_position()
        self.time=0
        self.rotation=randint(0, 360)
        self.color=Color(255, 234, 0)
        self.add_tag('enemy')
        self.health = 5
        self.enemyhealth = window.create_label()
        self.enemyhealth.text = "enemy health = "+ str(self.health)
        self.enemyhealth.font_size=11
        self.enemyhealth.x=self.x-self.width/2
        self.enemyhealth.y=self.y-self.height/2

    def on_update(self, dt):
        self.move_forward(3)
        if self.is_touching_any_sprite_with_tag('barrier'):
            self.delete()
        if self.is_touching_any_sprite_with_tag('bullet'):
            self.health-=1
        if self.is_touching_window_edge():
            self.delete()
        self.time+=dt
        if self.time>0.5:
            b=window.create_sprite(EnemyBullet)
            b.position=self.position
            b.point_toward_sprite(player)
            self.time=0
        self.enemyhealth.x=self.x-self.width/2
        self.enemyhealth.y=self.y-self.height/2
        self.enemyhealth.text = "enemy health = "+ str(self.health)
        if self.health<=0:
            self.delete()

    def delete(self):
        self.enemyhealth.delete()
        return super().delete()
```