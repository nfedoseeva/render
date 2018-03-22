import bpy
import random
import math
from random import uniform
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
import logging
import argparse

scene = bpy.context.scene
alpha = 1.5707963705062866 #90 degree angle
beta = 3.1415927410125732 #180
# robot 000
b0 = scene.objects["Base.000"]
s0 = scene.objects["Shoulder.000"]
u0 = scene.objects["Upperarm.000"]
f0 = scene.objects["Forearm.000"]
w10 = scene.objects["Wrist1.000"]
w20 = scene.objects["Wrist2.000"]
w30 = scene.objects["Wrist3.000"]
# robot 001
b1 = scene.objects["Base.001"]
s1 = scene.objects["Shoulder.001"]
u1 = scene.objects["Upperarm.001"]
f1 = scene.objects["Forearm.001"]
w11 = scene.objects["Wrist1.001"]
w21 = scene.objects["Wrist2.001"]
w31 = scene.objects["Wrist3.001"]
# robot 002
b2 = scene.objects["Base.002"]
s2 = scene.objects["Shoulder.002"]
u2 = scene.objects["Upperarm.002"]
f2 = scene.objects["Forearm.002"]
w12 = scene.objects["Wrist1.002"]
w22 = scene.objects["Wrist2.002"]
w32 = scene.objects["Wrist3.002"]
# robot 003
b3 = scene.objects["Base.003"]
s3 = scene.objects["Shoulder.003"]
u3 = scene.objects["Upperarm.003"]
f3 = scene.objects["Forearm.003"]
w13 = scene.objects["Wrist1.003"]
w23 = scene.objects["Wrist2.003"]
w33 = scene.objects["Wrist3.003"]

#robot 000 control
s0.rotation_euler = (0,0,alpha)
u0.rotation_euler = (0,alpha,0)
f0.rotation_euler = (0,alpha,0)
w10.rotation_euler = (0,alpha,0)
w20.rotation_euler = (0,0,alpha)
w30.rotation_euler = (0,alpha,0)
#robot 001 control
s1.rotation_euler = (0,0,alpha)
u1.rotation_euler = (0,alpha,0)
f1.rotation_euler = (0,alpha,0)
w11.rotation_euler = (0,alpha,0)
w21.rotation_euler = (0,0,alpha)
w31.rotation_euler = (0,alpha,0)
#robot 002 control
s2.rotation_euler = (0,0,alpha)
u2.rotation_euler = (0,alpha,0)
f2.rotation_euler = (0,alpha,0)
w12.rotation_euler = (0,alpha,0)
w22.rotation_euler = (0,0,alpha)
w32.rotation_euler = (0,alpha,0)
#robot 003 control
s3.rotation_euler = (0,0,alpha)
u3.rotation_euler = (0,alpha,0)
f3.rotation_euler = (0,alpha,0)
w13.rotation_euler = (0,alpha,0)
w23.rotation_euler = (0,0,alpha)
w33.rotation_euler = (0,alpha,0)

#table control
tab0 = bpy.data.objects["table_000"]
tab0_loc = (-0.6,0.8,0.15)
tab1 = bpy.data.objects["table_001"]
tab1_loc = (0.6,0.8,0.15)
tab2 = bpy.data.objects["table_002"]
tab2_loc = (0.6,0.0,0.15)
tab3 = bpy.data.objects["table_003"]
tab3_loc = (-0.6,0.0,0.15)
tab4 = bpy.data.objects["table_004"]
tab4_loc = (0.6,-0.8,0.15)
tab5 = bpy.data.objects["table_005"]
tab5_loc = (-0.6,-0.8,0.15)

# available models
noah = scene.objects["Noah"]
adam = scene.objects["Adam"]
eve = scene.objects["Eve"] 


# ---------------------- kuka robot----------------------------
k_b = scene.objects["Kuka"]
k_s = scene.objects["kuka_shoulder"]
k_u = scene.objects["kuka_upperarm"]
k_e = scene.objects["kuka_elbow"]
k_a = scene.objects["kuka_arm"]
k_w1 = scene.objects["kuka_wrist1"]
k_w2 = scene.objects["kuka_wrist2"]
# kuka parts
kst1 = scene.objects["kuka_shoulder_tube_part_1"]
kst2 = scene.objects["kuka_shoulder_tube_part_2"]
kst3 = scene.objects["kuka_shoulder_tube_part_3"]
kst4 = scene.objects["kuka_shoulder_tube_part_4"]
kst5 = scene.objects["kuka_shoulder_tube_part_5"]
kst6 = scene.objects["kuka_shoulder_tube_part_6"]
kst7 = scene.objects["kuka_shoulder_tube_part_7"]
klk = scene.objects["kuka_letter_k"]
klu = scene.objects["kuka_letter_u"]
klk2 = scene.objects["kuka_letter_k_2"]
kla = scene.objects["kuka_letter_a"]
ket2 = scene.objects["kuka_elbow_tube_part_2"]
ket3 = scene.objects["kuka_elbow_tube_part_3"]
ket4 = scene.objects["kuka_elbow_tube_part_4"]
ket5 = scene.objects["kuka_elbow_tube_part_5"]
ket6 = scene.objects["kuka_elbow_tube_part_6"]
ket7 = scene.objects["kuka_elbow_tube_part_7"]
ket8 = scene.objects["kuka_elbow_tube_part_8"]
kt = scene.objects["kuka_tube"]
kt1 = scene.objects["kuka_tube_part_1"]
kt2 = scene.objects["kuka_tube_part_2"]
kt3 = scene.objects["kuka_tube_part_3"]
kt4 = scene.objects["kuka_tube_part_4"]
kt5 = scene.objects["kuka_tube_part_5"]
kt6 = scene.objects["kuka_tube_part_6"]
kt7 = scene.objects["kuka_tube_part_7"]
kb = scene.objects["kuka_base"]

k_b1 = scene.objects["Kuka.001"]
k_s1 = scene.objects["kuka_shoulder.001"]
k_u1 = scene.objects["kuka_upperarm.001"]
k_e1 = scene.objects["kuka_elbow.001"]
k_a1 = scene.objects["kuka_arm.001"]
k_w11 = scene.objects["kuka_wrist1.001"]
k_w21 = scene.objects["kuka_wrist2.001"]
# kuka parts
klk1 = scene.objects["kuka_letter_k.001"]
klu1 = scene.objects["kuka_letter_u.001"]
klk21 = scene.objects["kuka_letter_k_2.001"]
kla1 = scene.objects["kuka_letter_a.001"]
kb1 = scene.objects["kuka_base.001"]

# ---------------------- fanuc robot----------------------------
f_b = scene.objects["Fanuc"]
f_s = scene.objects["fanuc_shoulder"]
f_u = scene.objects["fanuc_upperarm"]
f_e = scene.objects["fanuc_elbow"]
f_a = scene.objects["fanuc_arm"]
f_w1 = scene.objects["fanuc_wrist1"]
f_w2 = scene.objects["fanuc_wrist2"]
f_w3 = scene.objects["fanuc_wrist3"]
f_we = scene.objects["fanuc_weird"]
f_b1 = scene.objects["Fanuc.001"]
f_s1 = scene.objects["fanuc_shoulder.001"]
f_u1 = scene.objects["fanuc_upperarm.001"]
f_e1 = scene.objects["fanuc_elbow.001"]
f_a1 = scene.objects["fanuc_arm.001"]
f_w11 = scene.objects["fanuc_wrist1.001"]
f_w21 = scene.objects["fanuc_wrist2.001"]
f_w31 = scene.objects["fanuc_wrist3.001"]
f_we1 = scene.objects["fanuc_weird.001"]

#camera control
_cam1 = bpy.data.objects["Camera"]  
_cam1.location = Vector((0,0,1.5)) 

#light control
lamp1 = scene.objects["Plane.001"]
lamp2 = scene.objects["Plane.002"]
lamp3 = scene.objects["Plane.003"]
lamp4 = scene.objects["Plane.004"]
lamp5 = scene.objects["Plane.005"]
lamp6 = scene.objects["Plane.006"]
lamp7 = scene.objects["Plane.007"]
lamp8 = scene.objects["Plane.008"]
lamp9 = scene.objects["Plane.009"]
lamp10 = scene.objects["Plane.010"]
lamp11 = scene.objects["Plane.011"]
lamp12 = scene.objects["Plane.012"]
lamp13 = scene.objects["Plane.013"]
lamp14 = scene.objects["Plane.014"]
lamp15 = scene.objects["Plane.015"]
lamp16 = scene.objects["Plane.016"]
lamp17 = scene.objects["Plane.017"]
lamp18 = scene.objects["Plane.018"]
lamp19 = scene.objects["Plane.019"]
lamp20 = scene.objects["Plane.020"]
lamp21 = scene.objects["Plane.021"]
lamp22 = scene.objects["Plane.022"]
lamp23 = scene.objects["Plane.023"]
lamp24 = scene.objects["Plane.024"]
lamp25 = scene.objects["Plane.025"]
lamp26 = scene.objects["Plane.026"]
lamp27 = scene.objects["Plane.027"]
lamp28 = scene.objects["Plane.028"]
lamp29 = scene.objects["Plane.029"]
lamp30 = scene.objects["Plane.030"]
lamp31 = scene.objects["Plane.031"]
lamp32 = scene.objects["Plane.032"]
lamp33 = scene.objects["Plane.033"]

#frame control
fr = 0


#--------------------------------------------------------------------light control---------------------------------------------------------------------------

def lights_animation_render(iter):
	lamps = [lamp1, lamp2, lamp3, lamp4, lamp5,
	lamp6, lamp7, lamp8, lamp9, lamp10,
	lamp11, lamp12, lamp13, lamp14, lamp15,
	lamp16, lamp17, lamp18, lamp19, lamp20,
	lamp21, lamp22, lamp23, lamp24, lamp25,
	lamp26, lamp27, lamp28, lamp29, lamp30,
	lamp31, lamp32, lamp33]
	for l in lamps:
		l.hide_render = False
	fr = 0
	for i in range(0,iter):
		scene.frame_set(fr)
		for l in lamps:
			l.hide_render = random.sample(set([True,False]),1)[0]
			l.keyframe_insert(data_path="hide_render", index=-1)
			logging.warning(" Lamps animation set up in progress: " + str(fr) + " out of " + str(iter))
		fr += 1


#--------------------------------------------------------------------arms control---------------------------------------------------------------------------
def arms_animation_render(iter):
	fr = 0
	robo_details = (
			s0,u0,f0,w10,w20,w30,b0,
			s1,u1,f1,w11,w21,w31,b1,
			s2,u2,f2,w12,w22,w32,b2,
			s3,u3,f3,w13,w23,w33,b3,
			k_s,k_u,k_e,k_a,k_w1,k_w2,k_b,
			k_s1,k_u1,k_e1,k_a1,k_w11,k_w21,k_b1,
			f_s,f_u,f_e,f_a,f_w1,f_w2,f_b,
			f_s1,f_u1,f_e1,f_a1,f_w11,f_w21,f_b1)
	for i in range(0,iter):
		scene.frame_set(fr)
		for rd in robo_details:
			rd.hide_render = True
			rd.keyframe_insert(data_path="hide_render", index=-1)
		robo = random.sample(set([
			(s0,u0,f0,w10,w20,w30,b0),
			(s1,u1,f1,w11,w21,w31,b1),
			(s2,u2,f2,w12,w22,w32,b2),
			(s3,u3,f3,w13,w23,w33,b3),
			(k_s,k_u,k_e,k_a,k_w1,k_w2,k_b),
			(k_s1,k_u1,k_e1,k_a1,k_w11,k_w21,k_b1),
			(f_s,f_u,f_e,f_a,f_w1,f_w2,f_b),
			(f_s1,f_u1,f_e1,f_a1,f_w11,f_w21,f_b1)
			]),4)
		robohide1 = random.sample(set([True,False]),1)[0]
		robohide2 = random.sample(set([True,False]),1)[0]
		robohide3 = random.sample(set([True,False]),1)[0]
		robohide4 = random.sample(set([True,False]),1)[0]
		robohides = (robohide1,robohide2,robohide3,robohide4)
		for x in range(0,3):
			for y in range(0,7):
				robo[x][y].hide_render = robohides[x]
				robo[x][y].keyframe_insert(data_path="hide_render", index=-1)
		kuka_parts = (kst1,kst2,kst3,kst4,kst5,kst6,kst7,klk,klu,klk2,kla,ket2,ket3,ket4,ket5,ket6,ket7,ket8,kt,kt1,kt2,kt3,kt4,kt5,kt6,kt7,kb)
		kuka2_parts = (klk1,klu1,klk21,kla1,kb1)
		fanuc_parts = (f_we,f_w3)
		fanuc2_parts = (f_we1,f_w31)
		for kuka_part in kuka_parts:
			kuka_part.hide_render = k_s.hide_render
			kuka_part.keyframe_insert(data_path="hide_render", index=-1)
		for kuka2_part in kuka2_parts:
			kuka2_part.hide_render = k_s1.hide_render
			kuka2_part.keyframe_insert(data_path="hide_render", index=-1)
		for f_part in fanuc_parts:
			f_part.hide_render = f_s.hide_render
			f_part.keyframe_insert(data_path="hide_render", index=-1)
		for f2_part in fanuc2_parts:
			f2_part.hide_render = f_s1.hide_render
			f2_part.keyframe_insert(data_path="hide_render", index=-1)
		logging.warning(" Arms visibility animation set up in progress: " + str(fr) + " out of " + str(iter))
		fr += 1



def genListRotArm(num):
	l = [0]
	for x in range (0,num):
		l2 = random.uniform(-1.5,1.5)
		l = l + [l2]
	return l


def genListRotKuka_upperarm(num):
	l = [0]
	for x in range (0,num):
		l2 = random.uniform(-0.7853981852531433,2.094395160675049)
		l = l + [l2]
	return l

def genListRotFanuc_upperarm(num):
	l = [0]
	for x in range (0,num):
		l2 = random.uniform(-0.9599310755729675,2.094395160675049)
		l = l + [l2]
	return l

def genListRotFanuc_elbow(num):
	l = [0]
	for x in range (0,num):
		l2 = random.uniform(-3.7507123947143555,0.9599310755729675)
		l = l + [l2]
	return l

def genListRotKuka_elbow(num):
	l = [0]
	for x in range (0,num):
		l2 = random.uniform(-2.0071287155151367,0.4363323152065277)
		l = l + [l2]
	return l

def genListRotKuka_wrist1(num):
	l = [0]
	for x in range (0,num):
		l2 = random.uniform(-2.268928050994873,2.0071287155151367)
		l = l + [l2]
	return l

def genListRotFanuc_wrist1(num):
	l = [0]
	for x in range (0,num):
		l2 = random.uniform(-3.0455892086029053,0.4363323152065277)
		l = l + [l2]
	return l

def genListRotKuka_360(num):
	l = [0]
	for x in range (0,num):
		l2 = random.uniform(0.0,6.2831854820251465)
		l = l + [l2]
	return l

def arms_animation_rot(iter):
	s0_rots = genListRotArm(iter)
	u0_rots = genListRotArm(iter)
	f0_rots = genListRotArm(iter)
	w10_rots = genListRotArm(iter)
	w20_rots = genListRotArm(iter)
	w30_rots = genListRotArm(iter)
	s1_rots = genListRotArm(iter)
	u1_rots = genListRotArm(iter)
	f1_rots = genListRotArm(iter)
	w11_rots = genListRotArm(iter)
	w21_rots = genListRotArm(iter)
	w31_rots = genListRotArm(iter)
	s2_rots = genListRotArm(iter)
	u2_rots = genListRotArm(iter)
	f2_rots = genListRotArm(iter)
	w12_rots = genListRotArm(iter)
	w22_rots = genListRotArm(iter)
	w32_rots = genListRotArm(iter)
	s3_rots = genListRotArm(iter)
	u3_rots = genListRotArm(iter)
	f3_rots = genListRotArm(iter)
	w13_rots = genListRotArm(iter)
	w23_rots = genListRotArm(iter)
	w33_rots = genListRotArm(iter)
	# k_b_rots = genListRotKuka_360(iter)
	k_s_rots = genListRotKuka_360(iter)
	k_u_rots = genListRotKuka_upperarm(iter)
	k_e_rots = genListRotKuka_elbow(iter)
	k_a_rots = genListRotKuka_360(iter)
	k_w1_rots = genListRotKuka_wrist1(iter)
	k_w2_rots = genListRotKuka_360(iter)
	k_s1_rots = genListRotKuka_360(iter)
	k_u1_rots = genListRotKuka_upperarm(iter)
	k_e1_rots = genListRotKuka_elbow(iter)
	k_a1_rots = genListRotKuka_360(iter)
	k_w11_rots = genListRotKuka_wrist1(iter)
	k_w21_rots = genListRotKuka_360(iter)
	# fanuc rotation
	f_s_rots = genListRotKuka_360(iter)
	f_s1_rots = genListRotKuka_360(iter)
	f_u_rots = genListRotFanuc_upperarm(iter)
	f_u1_rots = genListRotFanuc_upperarm(iter)
	f_a_rots = genListRotKuka_360(iter)
	f_a1_rots = genListRotKuka_360(iter)
	f_e_rots = genListRotKuka_elbow(iter)
	f_e1_rots = genListRotKuka_elbow(iter)
	f_w1_rots = genListRotFanuc_wrist1(iter)
	f_w2_rots = genListRotKuka_360(iter)
	f_w11_rots = genListRotFanuc_wrist1(iter)
	f_w21_rots = genListRotKuka_360(iter)
	f_w3_rots = genListRotKuka_360(iter)
	f_w31_rots = genListRotKuka_360(iter)
	fr = 0
	# robo_details(
	# 		s0,u0,f0,w10,w20,w30,
	# 		s1,u1,f1,w11,w21,w31,
	# 		s2,u2,f2,w12,w22,w32,
	# 		s3,u3,f3,w13,w23,w33,
	# 		k_s,k_u,k_e,k_a,k_w1,k_w2,
	# 		k_s1,k_u1,k_e1,k_a1,k_w11,k_w21,
	# 		f_s,f_u,f_e,f_a,f_w1,f_w2,f_w3,
	# 		f_s1,f_u1,f_e1,f_a1,f_w11,f_w21,f_w31)
	# robo_rots(
	# 		s0_rots,u0_rots,f0_rots,w10_rots,w20_rots,w30_rots,
	# 		s1_rots,u1_rots,f1_rots,w11_rots,w21_rots,w31_rots,
	# 		s2_rots,u2_rots,f2_rots,w12_rots,w22_rots,w32_rots,
	# 		s3_rots,u3_rots,f3_rots,w13_rots,w23_rots,w33_rots,
	# 		k_s_rots,k_u_rots,k_e_rots,k_a_rots,k_w1_rots,k_w2_rots,
	# 		k_s1_rots,k_u1_rots,k_e1_rots,k_a1_rots,k_w11_rots,k_w21_rots,
	# 		f_s_rots,f_u,f_e_rots,f_a_rots,f_w1_rots,f_w2_rots,f_w3_rots,
	# 		f_s1_rots,f_u1_rots,f_e1_rots,f_a1_rots,f_w11_rots,f_w21_rots,f_w31_rots)
	for x in range(0,iter):
		scene.frame_set(fr)
		#0
		s0.rotation_euler.z = s0_rots[x]
		s0.keyframe_insert(data_path="rotation_euler", index=-1)
		u0.rotation_euler.y = u0_rots[x]
		u0.keyframe_insert(data_path="rotation_euler", index=-1)
		f0.rotation_euler.y = f0_rots[x]
		f0.keyframe_insert(data_path="rotation_euler", index=-1)
		w10.rotation_euler.y = w10_rots[x]
		w10.keyframe_insert(data_path="rotation_euler", index=-1)
		w20.rotation_euler.z = w20_rots[x]
		w20.keyframe_insert(data_path="rotation_euler", index=-1)
		w30.rotation_euler.y = w30_rots[x]
		w30.keyframe_insert(data_path="rotation_euler", index=-1)
		#1
		s1.rotation_euler.z = s1_rots[x]
		s1.keyframe_insert(data_path="rotation_euler", index=-1)
		u1.rotation_euler.y = u1_rots[x]
		u1.keyframe_insert(data_path="rotation_euler", index=-1)
		f1.rotation_euler.y = f1_rots[x]
		f1.keyframe_insert(data_path="rotation_euler", index=-1)
		w11.rotation_euler.y = w11_rots[x]
		w11.keyframe_insert(data_path="rotation_euler", index=-1)
		w21.rotation_euler.z = w21_rots[x]
		w21.keyframe_insert(data_path="rotation_euler", index=-1)
		w31.rotation_euler.y = w31_rots[x]
		w31.keyframe_insert(data_path="rotation_euler", index=-1)
		#2
		s2.rotation_euler.z = s2_rots[x]
		s2.keyframe_insert(data_path="rotation_euler", index=-1)
		u2.rotation_euler.y = u2_rots[x]
		u2.keyframe_insert(data_path="rotation_euler", index=-1)
		f2.rotation_euler.y = f2_rots[x]
		f2.keyframe_insert(data_path="rotation_euler", index=-1)
		w12.rotation_euler.y = w12_rots[x]
		w12.keyframe_insert(data_path="rotation_euler", index=-1)
		w22.rotation_euler.z = w22_rots[x]
		w22.keyframe_insert(data_path="rotation_euler", index=-1)
		w32.rotation_euler.y = w32_rots[x]
		w32.keyframe_insert(data_path="rotation_euler", index=-1)
		#3
		s3.rotation_euler.z = s3_rots[x]
		s3.keyframe_insert(data_path="rotation_euler", index=-1)
		u3.rotation_euler.y = u3_rots[x]
		u3.keyframe_insert(data_path="rotation_euler", index=-1)
		f3.rotation_euler.y = f3_rots[x]
		f3.keyframe_insert(data_path="rotation_euler", index=-1)
		w13.rotation_euler.y = w13_rots[x]
		w13.keyframe_insert(data_path="rotation_euler", index=-1)
		w23.rotation_euler.z = w23_rots[x]
		w23.keyframe_insert(data_path="rotation_euler", index=-1)
		w33.rotation_euler.y = w33_rots[x]
		w33.keyframe_insert(data_path="rotation_euler", index=-1)
		#kuka
		k_s.rotation_euler.z = k_s_rots[x]
		k_s.keyframe_insert(data_path="rotation_euler", index=-1)
		k_u.rotation_euler.y = k_u_rots[x]
		k_u.keyframe_insert(data_path="rotation_euler", index=-1)
		k_e.rotation_euler.y = k_e_rots[x]
		k_e.keyframe_insert(data_path="rotation_euler", index=-1)
		k_a.rotation_euler.x = k_a_rots[x]
		k_a.keyframe_insert(data_path="rotation_euler", index=-1)
		k_w1.rotation_euler.y = k_w1_rots[x]
		k_w1.keyframe_insert(data_path="rotation_euler", index=-1)
		k_w2.rotation_euler.x = k_w2_rots[x]
		k_w2.keyframe_insert(data_path="rotation_euler", index=-1)
		#kuka 2
		k_s1.rotation_euler.z = k_s1_rots[x]
		k_s1.keyframe_insert(data_path="rotation_euler", index=-1)
		k_u1.rotation_euler.y = k_u1_rots[x]
		k_u1.keyframe_insert(data_path="rotation_euler", index=-1)
		k_e1.rotation_euler.y = k_e1_rots[x]
		k_e1.keyframe_insert(data_path="rotation_euler", index=-1)
		k_a1.rotation_euler.x = k_a1_rots[x]
		k_a1.keyframe_insert(data_path="rotation_euler", index=-1)
		k_w11.rotation_euler.y = k_w11_rots[x]
		k_w11.keyframe_insert(data_path="rotation_euler", index=-1)
		k_w21.rotation_euler.x = k_w21_rots[x]
		k_w21.keyframe_insert(data_path="rotation_euler", index=-1)
		#fanuc
		f_s.rotation_euler.z = f_s_rots[x]
		f_s.keyframe_insert(data_path="rotation_euler", index=-1)
		f_u.rotation_euler.y = f_u_rots[x]
		f_u.keyframe_insert(data_path="rotation_euler", index=-1)
		f_e.rotation_euler.y = f_e_rots[x]
		f_e.keyframe_insert(data_path="rotation_euler", index=-1)
		f_a.rotation_euler.x = f_a_rots[x]
		f_a.keyframe_insert(data_path="rotation_euler", index=-1)
		f_w1.rotation_euler.y = f_w1_rots[x]
		f_w1.keyframe_insert(data_path="rotation_euler", index=-1)
		f_w2.rotation_euler.x = f_w2_rots[x]
		f_w2.keyframe_insert(data_path="rotation_euler", index=-1)
		f_w3.rotation_euler.x = f_w3_rots[x]
		f_w3.keyframe_insert(data_path="rotation_euler", index=-1)
		#fanuc 2
		f_s1.rotation_euler.z = f_s1_rots[x]
		f_s1.keyframe_insert(data_path="rotation_euler", index=-1)
		f_u1.rotation_euler.y = f_u1_rots[x]
		f_u1.keyframe_insert(data_path="rotation_euler", index=-1)
		f_e1.rotation_euler.y = f_e1_rots[x]
		f_e1.keyframe_insert(data_path="rotation_euler", index=-1)
		f_a1.rotation_euler.x = f_a1_rots[x]
		f_a1.keyframe_insert(data_path="rotation_euler", index=-1)
		f_w11.rotation_euler.y = f_w11_rots[x]
		f_w11.keyframe_insert(data_path="rotation_euler", index=-1)
		f_w21.rotation_euler.x = f_w21_rots[x]
		f_w21.keyframe_insert(data_path="rotation_euler", index=-1)
		f_w31.rotation_euler.x = f_w31_rots[x]
		f_w31.keyframe_insert(data_path="rotation_euler", index=-1)
		logging.warning(" Arms rotation animation set up in progress: " + str(fr) + " out of " + str(iter))
		fr += 1 


# -------------------------------------------------table animation------------------------------------------
def table_init():
	tab0.location = tab0_loc
	tab0.keyframe_insert(data_path="location", index=-1)
	tab1.location = tab1_loc
	tab1.keyframe_insert(data_path="location", index=-1)
	tab2.location = tab2_loc
	tab2.keyframe_insert(data_path="location", index=-1)
	tab3.location = tab3_loc
	tab3.keyframe_insert(data_path="location", index=-1)
	tab4.location = tab4_loc
	tab4.keyframe_insert(data_path="location", index=-1)
	tab5.location = tab5_loc
	tab5.keyframe_insert(data_path="location", index=-1)

def set_table(iter):
	fr = 0
	for x in range(0,iter):
		scene.frame_set(fr)
		table_init()
		ifmove = random.sample(set([True,False]),1)[0]
		if ifmove == True:
			table_move(random.sample(set([0,1]),1)[0])
		else:
			table_init()
		fr += 1


def table_move(x):
	if x == 0:
		# if so -- the movement will affect only x axis
		x_tab = random.sample(set([(tab0,tab1),(tab2,tab3),(tab4,tab5)]),1)[0]
		x_move = random.sample(set([0.10,-0.10]),1)[0]
		x_tab[0].location.x += x_move
		x_tab[0].keyframe_insert(data_path="location", index=-1)
		x_tab[1].location.x += x_move
		x_tab[1].keyframe_insert(data_path="location", index=-1)
	else:
		if x == 1:
			y_tab = random.sample(set([(tab0,tab3,tab5),(tab2,tab4,tab1)]),1)[0]
			y_move = random.sample(set([0.10,-0.10]),1)[0]
			y_tab[0].location.y += y_move
			y_tab[0].keyframe_insert(data_path="location", index=-1)
			y_tab[1].location.y += y_move
			y_tab[1].keyframe_insert(data_path="location", index=-1)
			y_tab[2].location.y += y_move
			y_tab[2].keyframe_insert(data_path="location", index=-1)


# ------------------------------------------------markers generation----------------------------------------

def marker_init():
	for y in range(0,24):
		set_marker(y,True)

def choose_markers():
	for x in range(0,24):
		choice = random.sample(set([True,False]),1)[0]
		set_marker(x,choice)

def set_marker(marker_num,if_hide):
	bpy.data.objects["marker." + str('%03d' % (marker_num))].hide_render = if_hide
	bpy.data.objects["marker." + str('%03d' % (marker_num))].keyframe_insert(data_path="hide_render", index=-1)
	bpy.data.objects["marker_base." + str('%03d' % (marker_num))].hide_render = if_hide
	bpy.data.objects["marker_base." + str('%03d' % (marker_num))].keyframe_insert(data_path="hide_render", index=-1)
	bpy.data.objects["marker_white_base." + str('%03d' % (marker_num))].hide_render = if_hide
	bpy.data.objects["marker_white_base." + str('%03d' % (marker_num))].keyframe_insert(data_path="hide_render", index=-1)
	if if_hide == True:
		for x in range(0,40):
			bpy.data.objects["marker_" + str(x) + "." + str('%03d' % (marker_num))].hide_render = if_hide
			bpy.data.objects["marker_" + str(x) + "." + str('%03d' % (marker_num))].keyframe_insert(data_path="hide_render", index=-1)
	else:
		if if_hide == False:
			for x in range(0,40):
				# bpy.data.objects["marker_" + str(x) + "." + str('%03d' % (marker_num))].hide_render = False
				bpy.data.objects["marker_" + str(x) + "." + str('%03d' % (marker_num))].hide_render = random.sample(set([True,False]),1)[0]
				bpy.data.objects["marker_" + str(x) + "." + str('%03d' % (marker_num))].keyframe_insert(data_path="hide_render", index=-1)


def set_markers(frs):
	fr = 0
	for x in range(0,frs):
		scene.frame_set(fr)
		choose_markers()
		fr += 1


# -------------------------------------------------animation launch------------------------------------------
def set_keys_main(keys_num):
	set_table(keys_num)
	logging.warning(" Table is ready")
	set_markers(keys_num)
	logging.warning(" Markers are ready")
	arms_animation_render(keys_num)
	logging.warning(" Arms visibility animation is ready")
	arms_animation_rot(keys_num)
	logging.warning(" Arms rotation animation is ready")
	lights_animation_render(keys_num)
	logging.warning(" Lights animation is ready")
	bpy.ops.wm.save_mainfile()
	logging.warning(" Main file is saved")
	logging.warning(" Main animation is set")



# -----------------------------------------parsing args-----------------------------------------------------
# logging.warning(" Script is installed, I guess")

# def get_args():
# 	parser = argparse.ArgumentParser()
# 	_, all_arguments = parser.parse_known_args()
# 	double_dash_index = all_arguments.index('--')
# 	script_args = all_arguments[double_dash_index + 1: ]
# 	parser.add_argument('-k', '--keys', help="number of key frames for one animation")
# 	parsed_script_args, _ = parser.parse_known_args(script_args)
# 	return parsed_script_args
	
# args = get_args()
# _keys = int(args.keys)
set_keys_main(100)

