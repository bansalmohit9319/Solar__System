from vpython import *
import math, random, os


def try_texture(fname):
    if os.path.isfile(fname):
        return fname  
    return None


planet_data = [
    ("Mercury", 0.39, 0.383, "mercury.jpg", color.gray(0.6), 0),
    ("Venus",   0.72, 0.95,  "venus.jpg",   color.orange, 0),
    ("Earth",   1.00, 1.00,  "earth.jpg",   color.blue,   1),
    ("Mars",    1.52, 0.532, "mars.jpg",    color.red,    2),
    ("Jupiter", 5.20, 11.21, "jupiter.jpg", color.orange, 4),
    ("Saturn",  9.58, 9.45,  "saturn.jpg",  color.yellow, 7),
    ("Uranus",  19.18,4.01,  "uranus.jpg",  color.cyan,   3),
    ("Neptune", 30.07,3.88,  "neptune.jpg", color.blue,   2),
    ("Pluto",   39.48,0.186, "pluto.jpg",   color.white,  1)
]


DIST_SCALE = 2.5    
SIZE_SCALE = 0.18   
MOON_SCALE = 0.06


scene.title = "3D Solar System (VPython) — textures if available"
scene.width = 1000
scene.height = 700
scene.background = color.black
scene.range = 35


num_stars = 400
stars = []
for i in range(num_stars):
    x = random.uniform(-120, 120)
    y = random.uniform(-120, 120)
    z = random.uniform(-40, 40)
    s = sphere(pos=vector(x,y,z), radius=0.07, color=color.white, emissive=True, opacity=0.8)
    stars.append(s)


sun = sphere(pos=vector(0,0,0), radius=2.5, color=vector(1,0.8,0.0), emissive=True)

sun_glow = sphere(pos=sun.pos, radius=3.2, color=color.yellow, opacity=0.08)


planets = []
moons_all = []
for name, dist_au, rel_radius, tex_file, fallback_color, moon_count in planet_data:
    dist = dist_au * DIST_SCALE
    radius = rel_radius * SIZE_SCALE

    
    tex = try_texture(tex_file)

    if tex:
        p = sphere(pos=vector(dist,0,0), radius=radius, texture=tex, make_trail=False)
    else:
        p = sphere(pos=vector(dist,0,0), radius=radius, color=fallback_color, make_trail=False)

    
    p.name = name
    p.orbit_radius = dist
    p.orbit_speed = 0.8 * (1.0 / (1 + dist_au**0.5))  
    planets.append(p)

    
    moons = []
    for m in range(moon_count):
        mrad = radius * (0.3 + 0.2*m) + MOON_SCALE
        
        theta = random.uniform(0, 2*math.pi)
        mx = p.pos.x + mrad * math.cos(theta)
        my = p.pos.y + mrad * math.sin(theta)
        mz = p.pos.z + 0.05 * m  
        
        moon_tex = try_texture("moon.jpg")
        if moon_tex:
            moon = sphere(pos=vector(mx,my,mz), radius=mrad*0.35, texture=moon_tex)
        else:
            moon = sphere(pos=vector(mx,my,mz), radius=mrad*0.35, color=color.white*0.9)
        moon.orbit_radius = mrad
        moon.orbit_speed = 2.0 + 0.6*m  
        moons.append(moon)
    moons_all.append(moons)


 
for p in planets:
    if p.name.lower() == "saturn":
        sat = p
        break
else:
    sat = None

if sat:
    ring_inner = sat.radius * 1.4
    ring_outer = sat.radius * 3.0
    ring_count = 140
    ring_objs = []
    for i in range(ring_count):
        angle = (2*math.pi) * (i / ring_count)
        r = random.uniform(ring_inner, ring_outer)
        x = sat.pos.x + r * math.cos(angle)
        y = sat.pos.y + r * math.sin(angle)
        z = sat.pos.z + random.uniform(-0.02, 0.02)
        
        part = box(pos=vector(x,y,z), length=0.06, height=0.02, width=0.02, color=vector(0.9,0.8,0.6), opacity=0.9)
        ring_objs.append(part)


for p in planets:
    pts = []
    for t in range(180):
        th = 2*math.pi * (t/180)
        x = p.orbit_radius * math.cos(th)
        y = p.orbit_radius * math.sin(th)
        pts.append(vector(x,y,0))
    curve(points=pts, color=color.white, radius=0.005, opacity=0.25)


t = 0
dt = 0.02
while True:
    rate(60)
    t += dt
    
    scene.forward = vector(-0.3*math.cos(t*0.03), -0.3*math.sin(t*0.03), -0.6)

    for i, p in enumerate(planets):
        
        ang = t * p.orbit_speed
        x = p.orbit_radius * math.cos(ang)
        y = p.orbit_radius * math.sin(ang)
        z = 0.0
        p.pos = vector(x, y, z)

        
        p.rotate(angle=0.01 + 0.002*i, axis=vector(0,0,1))

        
        moons = moons_all[i]
        for j, m in enumerate(moons):
            mang = t * m.orbit_speed
            mr = m.orbit_radius
            mx = p.pos.x + mr * math.cos(mang)
            my = p.pos.y + mr * math.sin(mang)
            mz = p.pos.z + 0.02 * j
            m.pos = vector(mx, my, mz)

from vpython import *
import math, random, os


def try_texture(fname):
    if os.path.isfile(fname):
        return fname  
    return None


planet_data = [
    ("Mercury", 0.39, 0.383, "mercury.jpg", color.gray(0.6), 0),
    ("Venus",   0.72, 0.95,  "venus.jpg",   color.orange, 0),
    ("Earth",   1.00, 1.00,  "earth.jpg",   color.blue,   1),
    ("Mars",    1.52, 0.532, "mars.jpg",    color.red,    2),
    ("Jupiter", 5.20, 11.21, "jupiter.jpg", color.orange, 4),
    ("Saturn",  9.58, 9.45,  "saturn.jpg",  color.yellow, 7),
    ("Uranus",  19.18,4.01,  "uranus.jpg",  color.cyan,   3),
    ("Neptune", 30.07,3.88,  "neptune.jpg", color.blue,   2),
    ("Pluto",   39.48,0.186, "pluto.jpg",   color.white,  1)
]


DIST_SCALE = 2.5    
SIZE_SCALE = 0.18   
MOON_SCALE = 0.06


scene.title = "3D Solar System (VPython) — textures if available"
scene.width = 1000
scene.height = 700
scene.background = color.black
scene.range = 35


num_stars = 400
stars = []
for i in range(num_stars):
    x = random.uniform(-120, 120)
    y = random.uniform(-120, 120)
    z = random.uniform(-40, 40)
    s = sphere(pos=vector(x,y,z), radius=0.07, color=color.white, emissive=True, opacity=0.8)
    stars.append(s)


sun = sphere(pos=vector(0,0,0), radius=2.5, color=vector(1,0.8,0.0), emissive=True)

sun_glow = sphere(pos=sun.pos, radius=3.2, color=color.yellow, opacity=0.08)


planets = []
moons_all = []
for name, dist_au, rel_radius, tex_file, fallback_color, moon_count in planet_data:
    dist = dist_au * DIST_SCALE
    radius = rel_radius * SIZE_SCALE

    
    tex = try_texture(tex_file)

    if tex:
        p = sphere(pos=vector(dist,0,0), radius=radius, texture=tex, make_trail=False)
    else:
        p = sphere(pos=vector(dist,0,0), radius=radius, color=fallback_color, make_trail=False)

    
    p.name = name
    p.orbit_radius = dist
    p.orbit_speed = 0.8 * (1.0 / (1 + dist_au**0.5))  
    planets.append(p)

    
    moons = []
    for m in range(moon_count):
        mrad = radius * (0.3 + 0.2*m) + MOON_SCALE
        
        theta = random.uniform(0, 2*math.pi)
        mx = p.pos.x + mrad * math.cos(theta)
        my = p.pos.y + mrad * math.sin(theta)
        mz = p.pos.z + 0.05 * m  
        
        moon_tex = try_texture("moon.jpg")
        if moon_tex:
            moon = sphere(pos=vector(mx,my,mz), radius=mrad*0.35, texture=moon_tex)
        else:
            moon = sphere(pos=vector(mx,my,mz), radius=mrad*0.35, color=color.white*0.9)
        moon.orbit_radius = mrad
        moon.orbit_speed = 2.0 + 0.6*m  
        moons.append(moon)
    moons_all.append(moons)


for p in planets:
    if p.name.lower() == "saturn":
        sat = p
        break
else:
    sat = None

if sat:
    ring_inner = sat.radius * 1.4
    ring_outer = sat.radius * 3.0
    ring_count = 140
    ring_objs = []
    for i in range(ring_count):
        angle = (2*math.pi) * (i / ring_count)
        r = random.uniform(ring_inner, ring_outer)
        x = sat.pos.x + r * math.cos(angle)
        y = sat.pos.y + r * math.sin(angle)
        z = sat.pos.z + random.uniform(-0.02, 0.02)
        
        part = box(pos=vector(x,y,z), length=0.06, height=0.02, width=0.02, color=vector(0.9,0.8,0.6), opacity=0.9)
        ring_objs.append(part)


for p in planets:
    pts = []
    for t in range(180):
        th = 2*math.pi * (t/180)
        x = p.orbit_radius * math.cos(th)
        y = p.orbit_radius * math.sin(th)
        pts.append(vector(x,y,0))
    curve(points=pts, color=color.white, radius=0.005, opacity=0.25)


t = 0
dt = 0.02
while True:
    rate(60)
    t += dt
    
    scene.forward = vector(-0.3*math.cos(t*0.03), -0.3*math.sin(t*0.03), -0.6)

    for i, p in enumerate(planets):
        
        ang = t * p.orbit_speed
        x = p.orbit_radius * math.cos(ang)
        y = p.orbit_radius * math.sin(ang)
        z = 0.0
        p.pos = vector(x, y, z)

        
        p.rotate(angle=0.01 + 0.002*i, axis=vector(0,0,1))

        
        moons = moons_all[i]
        for j, m in enumerate(moons):
            mang = t * m.orbit_speed
            mr = m.orbit_radius
            mx = p.pos.x + mr * math.cos(mang)
            my = p.pos.y + mr * math.sin(mang)
            mz = p.pos.z + 0.02 * j
            m.pos = vector(mx, my, mz)

from vpython import *
import math, random, os


def try_texture(fname):
    if os.path.isfile(fname):
        return fname  
    return None


planet_data = [
    ("Mercury", 0.39, 0.383, "mercury.jpg", color.gray(0.6), 0),
    ("Venus",   0.72, 0.95,  "venus.jpg",   color.orange, 0),
    ("Earth",   1.00, 1.00,  "earth.jpg",   color.blue,   1),
    ("Mars",    1.52, 0.532, "mars.jpg",    color.red,    2),
    ("Jupiter", 5.20, 11.21, "jupiter.jpg", color.orange, 4),
    ("Saturn",  9.58, 9.45,  "saturn.jpg",  color.yellow, 7),
    ("Uranus",  19.18,4.01,  "uranus.jpg",  color.cyan,   3),
    ("Neptune", 30.07,3.88,  "neptune.jpg", color.blue,   2),
    ("Pluto",   39.48,0.186, "pluto.jpg",   color.white,  1)
]


DIST_SCALE = 2.5    
SIZE_SCALE = 0.18   
MOON_SCALE = 0.06


scene.title = "3D Solar System (VPython) — textures if available"
scene.width = 1000
scene.height = 700
scene.background = color.black
scene.range = 35


num_stars = 400
stars = []
for i in range(num_stars):
    x = random.uniform(-120, 120)
    y = random.uniform(-120, 120)
    z = random.uniform(-40, 40)
    s = sphere(pos=vector(x,y,z), radius=0.07, color=color.white, emissive=True, opacity=0.8)
    stars.append(s)

sun = sphere(pos=vector(0,0,0), radius=2.5, color=vector(1,0.8,0.0), emissive=True)

sun_glow = sphere(pos=sun.pos, radius=3.2, color=color.yellow, opacity=0.08)


planets = []
moons_all = []
for name, dist_au, rel_radius, tex_file, fallback_color, moon_count in planet_data:
    dist = dist_au * DIST_SCALE
    radius = rel_radius * SIZE_SCALE

    
    tex = try_texture(tex_file)

    if tex:
        p = sphere(pos=vector(dist,0,0), radius=radius, texture=tex, make_trail=False)
    else:
        p = sphere(pos=vector(dist,0,0), radius=radius, color=fallback_color, make_trail=False)

    
    p.name = name
    p.orbit_radius = dist
    p.orbit_speed = 0.8 * (1.0 / (1 + dist_au**0.5))  
    planets.append(p)

    
    moons = []
    for m in range(moon_count):
        mrad = radius * (0.3 + 0.2*m) + MOON_SCALE
        
        theta = random.uniform(0, 2*math.pi)
        mx = p.pos.x + mrad * math.cos(theta)
        my = p.pos.y + mrad * math.sin(theta)
        mz = p.pos.z + 0.05 * m  
        
        moon_tex = try_texture("moon.jpg")
        if moon_tex:
            moon = sphere(pos=vector(mx,my,mz), radius=mrad*0.35, texture=moon_tex)
        else:
            moon = sphere(pos=vector(mx,my,mz), radius=mrad*0.35, color=color.white*0.9)
        moon.orbit_radius = mrad
        moon.orbit_speed = 2.0 + 0.6*m  
        moons.append(moon)
    moons_all.append(moons)


for p in planets:
    if p.name.lower() == "saturn":
        sat = p
        break
else:
    sat = None

if sat:
    ring_inner = sat.radius * 1.4
    ring_outer = sat.radius * 3.0
    ring_count = 140
    ring_objs = []
    for i in range(ring_count):
        angle = (2*math.pi) * (i / ring_count)
        r = random.uniform(ring_inner, ring_outer)
        x = sat.pos.x + r * math.cos(angle)
        y = sat.pos.y + r * math.sin(angle)
        z = sat.pos.z + random.uniform(-0.02, 0.02)
        
        part = box(pos=vector(x,y,z), length=0.06, height=0.02, width=0.02, color=vector(0.9,0.8,0.6), opacity=0.9)
        ring_objs.append(part)


for p in planets:
    pts = []
    for t in range(180):
        th = 2*math.pi * (t/180)
        x = p.orbit_radius * math.cos(th)
        y = p.orbit_radius * math.sin(th)
        pts.append(vector(x,y,0))
    curve(points=pts, color=color.white, radius=0.005, opacity=0.25)


t = 0
dt = 0.02
while True:
    rate(60)
    t += dt
    
    scene.forward = vector(-0.3*math.cos(t*0.03), -0.3*math.sin(t*0.03), -0.6)

    for i, p in enumerate(planets):
        
        ang = t * p.orbit_speed
        x = p.orbit_radius * math.cos(ang)
        y = p.orbit_radius * math.sin(ang)
        z = 0.0
        p.pos = vector(x, y, z)

        
        p.rotate(angle=0.01 + 0.002*i, axis=vector(0,0,1))

        
        moons = moons_all[i]
        for j, m in enumerate(moons):
            mang = t * m.orbit_speed
            mr = m.orbit_radius
            mx = p.pos.x + mr * math.cos(mang)
            my = p.pos.y + mr * math.sin(mang)
            mz = p.pos.z + 0.02 * j
            m.pos = vector(mx, my, mz)

