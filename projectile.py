import pygame as pg
from game_config import *
from move import *


def projectile_thrown(arme, projectile_thrown):
    # Speed of the projectile
    fx = 0
    fy = 0
    # If the projectile is thrown then its speed is equals to the force it's thrown
    if projectile_thrown:
        fy = GameConfig.FORCE_THROWN

    # Vitesse
    if arme.not_thrown():
        arme.vy = fy * GameConfig.DT * arme.coeff_vy
        arme.vx = fx * GameConfig.DT * arme.coeff_vx
    else:
        arme.vy = arme.vy + GameConfig.GRAVITY * GameConfig.DT
        arme.vx = fx + GameConfig.GRAVITY * GameConfig.DT * arme.coeff_vx

    # Position
    x = arme.rect.left
    vx_max = (arme.player.rect.left + x) / GameConfig.DT
    arme.vx = min(arme.vx, vx_max)

    y = arme.rect.top
    vy_max = (arme.player.rect.top - y) / GameConfig.DT
    arme.vy = min(arme.vy, vy_max)
    #print(arme.rect.top)
    #print(GameConfig.Y_PLATEFORM)
    if arme.rect.bottom == GameConfig.Y_PLATEFORM:
        print ("ok")
        arme.shootFinished = True
    arme.rect = arme.rect.move(arme.vx * GameConfig.DT, arme.vy * GameConfig.DT)
