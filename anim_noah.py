import bpy
import random
import math
from random import uniform
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
import logging
import argparse

scene = bpy.context.scene
table = scene.objects["table"]
alpha = 1.5707963705062866 #90 degree angle
beta = 3.1415927410125732 #180
empty = scene.objects["Empty"]
model = scene.objects["Noah"]
model.location.xy = Vector((0,0))
model.rotation_euler = (alpha,0,0)

#camera control
_cam1 = bpy.data.objects["Camera"] 
_cam1.location = Vector((0,0,1.5)) 

#frame control
fr = 0


#--------------------------------------------------------------------cam control---------------------------------------------------------------------------

def genListLoc(num):
	l = [(0,0,1)]
	for x in range (0,num):
		l2 = [(random.uniform(-2,2),random.uniform(-2,2),random.uniform(0.8,1.5))]
		l = l + l2
	return l



#--------------------------------------------------------------------model control---------------------------------------------------------------------------
def pointsCheck(frame,pt,camtxt,imgtxt,imgw,modeltxt,side):
	scene = bpy.context.scene
	scene.update()
	cam1 = bpy.data.objects["Camera"]
	locCam1 = Vector((cam1.matrix_world[0][3],cam1.matrix_world[1][3],cam1.matrix_world[2][3]))
	# kp = bpy.context.scene.objects['Keypoint']
	objA = bpy.context.scene.objects['Noah_A']
	objB = bpy.context.scene.objects['Noah_B']
	objC = bpy.context.scene.objects['Noah_C']
	objD = bpy.context.scene.objects['Noah_D']
	objE = bpy.context.scene.objects['Noah_E']
	objF = bpy.context.scene.objects['Noah_F']
	objG = bpy.context.scene.objects['Noah_G']
	objH = bpy.context.scene.objects['Noah_H']
	objI = bpy.context.scene.objects['Noah_I']
	objJ = bpy.context.scene.objects['Noah_J']
	objK = bpy.context.scene.objects['Noah_K']
	objL = bpy.context.scene.objects['Noah_L']
	objM = bpy.context.scene.objects['Noah_M']
	objN = bpy.context.scene.objects['Noah_N']
	objO = bpy.context.scene.objects['Noah_O']
	objP = bpy.context.scene.objects['Noah_P']
	objQ = bpy.context.scene.objects['Noah_Q']
	objR = bpy.context.scene.objects['Noah_R']
	objS = bpy.context.scene.objects['Noah_S']
	objT = bpy.context.scene.objects['Noah_T']
	objU = bpy.context.scene.objects['Noah_U']
	objV = bpy.context.scene.objects['Noah_V']
	objW = bpy.context.scene.objects['Noah_W']
	objX = bpy.context.scene.objects['Noah_X']
	cs, ce = cam1.data.clip_start, cam1.data.clip_end
	locA = Vector((objA.matrix_world[0][3],objA.matrix_world[1][3],objA.matrix_world[2][3]))
	locB = Vector((objB.matrix_world[0][3],objB.matrix_world[1][3],objB.matrix_world[2][3]))
	locC = Vector((objC.matrix_world[0][3],objC.matrix_world[1][3],objC.matrix_world[2][3]))
	locD = Vector((objD.matrix_world[0][3],objD.matrix_world[1][3],objD.matrix_world[2][3]))
	locE = Vector((objE.matrix_world[0][3],objE.matrix_world[1][3],objE.matrix_world[2][3]))
	locF = Vector((objF.matrix_world[0][3],objF.matrix_world[1][3],objF.matrix_world[2][3]))
	locG = Vector((objG.matrix_world[0][3],objG.matrix_world[1][3],objG.matrix_world[2][3]))
	locH = Vector((objH.matrix_world[0][3],objH.matrix_world[1][3],objH.matrix_world[2][3]))
	locI = Vector((objI.matrix_world[0][3],objI.matrix_world[1][3],objI.matrix_world[2][3]))
	locJ = Vector((objJ.matrix_world[0][3],objJ.matrix_world[1][3],objJ.matrix_world[2][3]))
	locK = Vector((objK.matrix_world[0][3],objK.matrix_world[1][3],objK.matrix_world[2][3]))
	locL = Vector((objL.matrix_world[0][3],objL.matrix_world[1][3],objL.matrix_world[2][3]))
	locM = Vector((objM.matrix_world[0][3],objM.matrix_world[1][3],objM.matrix_world[2][3]))
	locN = Vector((objN.matrix_world[0][3],objN.matrix_world[1][3],objN.matrix_world[2][3]))
	locO = Vector((objO.matrix_world[0][3],objO.matrix_world[1][3],objO.matrix_world[2][3]))
	locP = Vector((objP.matrix_world[0][3],objP.matrix_world[1][3],objP.matrix_world[2][3]))
	locQ = Vector((objQ.matrix_world[0][3],objQ.matrix_world[1][3],objQ.matrix_world[2][3]))
	locR = Vector((objR.matrix_world[0][3],objR.matrix_world[1][3],objR.matrix_world[2][3]))
	locS = Vector((objS.matrix_world[0][3],objS.matrix_world[1][3],objS.matrix_world[2][3]))
	locT = Vector((objT.matrix_world[0][3],objT.matrix_world[1][3],objT.matrix_world[2][3]))
	locU = Vector((objU.matrix_world[0][3],objU.matrix_world[1][3],objU.matrix_world[2][3]))
	locV = Vector((objV.matrix_world[0][3],objV.matrix_world[1][3],objV.matrix_world[2][3]))
	locW = Vector((objW.matrix_world[0][3],objW.matrix_world[1][3],objW.matrix_world[2][3]))
	locX = Vector((objX.matrix_world[0][3],objX.matrix_world[1][3],objX.matrix_world[2][3]))
	co_ndc_a = world_to_camera_view(scene, cam1, locA)
	co_ndc_b = world_to_camera_view(scene, cam1, locB)
	co_ndc_c = world_to_camera_view(scene, cam1, locC)
	co_ndc_d = world_to_camera_view(scene, cam1, locD)
	co_ndc_e = world_to_camera_view(scene, cam1, locE)
	co_ndc_f = world_to_camera_view(scene, cam1, locF)
	co_ndc_g = world_to_camera_view(scene, cam1, locG)
	co_ndc_h = world_to_camera_view(scene, cam1, locH)
	co_ndc_i = world_to_camera_view(scene, cam1, locI)
	co_ndc_j = world_to_camera_view(scene, cam1, locJ)
	co_ndc_k = world_to_camera_view(scene, cam1, locK)
	co_ndc_l = world_to_camera_view(scene, cam1, locL)
	co_ndc_m = world_to_camera_view(scene, cam1, locM)
	co_ndc_n = world_to_camera_view(scene, cam1, locN)
	co_ndc_o = world_to_camera_view(scene, cam1, locO)
	co_ndc_p = world_to_camera_view(scene, cam1, locP)
	co_ndc_q = world_to_camera_view(scene, cam1, locQ)
	co_ndc_r = world_to_camera_view(scene, cam1, locR)
	co_ndc_s = world_to_camera_view(scene, cam1, locS)
	co_ndc_t = world_to_camera_view(scene, cam1, locT)
	co_ndc_u = world_to_camera_view(scene, cam1, locU)
	co_ndc_v = world_to_camera_view(scene, cam1, locV)
	co_ndc_w = world_to_camera_view(scene, cam1, locW)
	co_ndc_x = world_to_camera_view(scene, cam1, locX)
	camtxt.write('%05d.png' % frame + ", " + str(cam1.matrix_world[0][3]) + ", " + str(cam1.matrix_world[1][3]) + ", " + str(cam1.matrix_world[2][3]) + ", " + str(empty.rotation_euler.x) + "\n")
	imgtxt.write('%05d.png' % frame + ", " + 
				str(co_ndc_a.x) + ", " + str(co_ndc_a.y) + ", " + 
				str(co_ndc_b.x) + ", " + str(co_ndc_b.y) + ", " + 
				str(co_ndc_c.x) + ", " + str(co_ndc_c.y) + ", " + 
				str(co_ndc_d.x) + ", " + str(co_ndc_d.y) + ", " + 
				str(co_ndc_e.x) + ", " + str(co_ndc_e.y) + ", " + 
				str(co_ndc_f.x) + ", " + str(co_ndc_f.y) + ", " + 
				str(co_ndc_g.x) + ", " + str(co_ndc_g.y) + ", " + 
				str(co_ndc_h.x) + ", " + str(co_ndc_h.y) + ", " + 
				str(co_ndc_i.x) + ", " + str(co_ndc_i.y) + ", " + 
				str(co_ndc_j.x) + ", " + str(co_ndc_j.y) + ", " + 
				str(co_ndc_k.x) + ", " + str(co_ndc_k.y) + ", " + 
				str(co_ndc_l.x) + ", " + str(co_ndc_l.y) + ", " + 
				str(co_ndc_m.x) + ", " + str(co_ndc_m.y) + ", " + 
				str(co_ndc_n.x) + ", " + str(co_ndc_n.y) + ", " + 
				str(co_ndc_o.x) + ", " + str(co_ndc_o.y) + ", " + 
				str(co_ndc_p.x) + ", " + str(co_ndc_p.y) + ", " + 
				str(co_ndc_q.x) + ", " + str(co_ndc_q.y) + ", " + 
				str(co_ndc_r.x) + ", " + str(co_ndc_r.y) + ", " + 
				str(co_ndc_s.x) + ", " + str(co_ndc_s.y) + ", " + 
				str(co_ndc_t.x) + ", " + str(co_ndc_t.y) + ", " + 
				str(co_ndc_u.x) + ", " + str(co_ndc_u.y) + ", " + 
				str(co_ndc_v.x) + ", " + str(co_ndc_v.y) + ", " + 
				str(co_ndc_w.x) + ", " + str(co_ndc_w.y) + ", " + 
				str(co_ndc_x.x) + ", " + str(co_ndc_x.y) + ", " +
				"\n")
	imgw.write('%05d.png' % frame + ", " + 
				str(locA[0]) + ", " + str(locA[1]) + ", " + str(locA[2]) + ", " + 
				str(locB[0]) + ", " + str(locB[1]) + ", " + str(locB[2]) + ", " + 
				str(locC[0]) + ", " + str(locC[1]) + ", " + str(locC[2]) + ", " + 
				str(locD[0]) + ", " + str(locD[1]) + ", " + str(locD[2]) + ", " + 
				str(locE[0]) + ", " + str(locE[1]) + ", " + str(locE[2]) + ", " + 
				str(locF[0]) + ", " + str(locF[1]) + ", " + str(locF[2]) + ", " + 
				str(locG[0]) + ", " + str(locG[1]) + ", " + str(locG[2]) + ", " + 
				str(locH[0]) + ", " + str(locH[1]) + ", " + str(locH[2]) + ", " +
				str(locI[0]) + ", " + str(locI[1]) + ", " + str(locI[2]) + ", " +
				str(locJ[0]) + ", " + str(locJ[1]) + ", " + str(locJ[2]) + ", " +
				str(locK[0]) + ", " + str(locK[1]) + ", " + str(locK[2]) + ", " +
				str(locL[0]) + ", " + str(locL[1]) + ", " + str(locL[2]) + ", " +
				str(locM[0]) + ", " + str(locM[1]) + ", " + str(locM[2]) + ", " +
				str(locN[0]) + ", " + str(locN[1]) + ", " + str(locN[2]) + ", " +
				str(locO[0]) + ", " + str(locO[1]) + ", " + str(locO[2]) + ", " +
				str(locP[0]) + ", " + str(locP[1]) + ", " + str(locP[2]) + ", " +
				str(locQ[0]) + ", " + str(locQ[1]) + ", " + str(locQ[2]) + ", " +
				str(locR[0]) + ", " + str(locR[1]) + ", " + str(locR[2]) + ", " +
				str(locS[0]) + ", " + str(locS[1]) + ", " + str(locS[2]) + ", " +
				str(locT[0]) + ", " + str(locT[1]) + ", " + str(locT[2]) + ", " +
				str(locU[0]) + ", " + str(locU[1]) + ", " + str(locU[2]) + ", " +
				str(locV[0]) + ", " + str(locV[1]) + ", " + str(locV[2]) + ", " +
				str(locW[0]) + ", " + str(locW[1]) + ", " + str(locW[2]) + ", " +
				str(locX[0]) + ", " + str(locX[1]) + ", " + str(locX[2]) + ", " +
				"\n")
	modeltxt.write('%05d.png' % frame + ", " + str(model.location.x) + ", " + str(model.location.y) + ", " + str(model.location.z) + ", " + 
		str(model.rotation_euler.x) + ", " + str(model.rotation_euler.y) + ", " + str(model.rotation_euler.z) + ", " + str(side) + "\n")
	# locations = (locA,locB,locC,locD,locE,locF,locG,locH,locI,locJ,locK, locL,locM,locN,locO,locP,locQ,locR,locS,locT,locU,locV,locW,locX)
	# keytxt.write('%05d.png' % frame + ", ")
	# for l in locations:
	# 	kp.matrix_world[0][3] = l[0]
	# 	kp.matrix_world[1][3] = l[1]
	# 	kp.matrix_world[2][3] = l[2]
	# 	keytxt.write(str(kp.location.x) + ", " + str(kp.location.y) + ", " + str(kp.location.z) + "; ")
	# keytxt.write("\n")

def emptyRots(e):
	l = [0]
	for x in range (0,e):
		r = random.randint(0,2)
		if (r > 0):
			l2 = 0
			l = l + [l2]
		else:
			l2 = random.uniform(-0.35, 0.35)
			l = l + [l2]
	return l

def genListRot(num):
	l = [0]
	for x in range (0,num):
		l2 = random.uniform(-beta,beta)
		l = l + [l2]
	return l


def model_cam_animation_render(iter, path_txt):
	empt_rot = emptyRots(iter)
	# _keytxt = open(path_txt + "keys.txt","w")
	_imgtxt1 = open(path_txt + "img1.txt","w")
	_camtxt1 = open(path_txt + "cam1.txt","w")
	_imgworld = open(path_txt + "imgworld.txt","w")
	_mod = open(path_txt + "model.txt","w")
	model_rots = genListRot(iter)
	_iter = int(iter / 20)
	cam_loc = genListLoc(iter)
	num_rots = 0
	fr = 0
	for x in range(0,_iter):
		for i in range(0,20):
			scene.frame_set(fr)
			model.location.xy = (random.uniform(-0.32, 0.32),random.uniform(-0.32, 0.32))
			model.keyframe_insert(data_path="location", index=-1)
			model.rotation_euler.z = model_rots[num_rots]
			model.keyframe_insert(data_path="rotation_euler", index=-1)
			model_xy = random.sample(set([(alpha,0),(0, alpha * 2),(alpha, alpha * 2),(alpha, alpha),(0,0)]),1)[0]
			model.rotation_euler.x = model_xy[0]
			model.rotation_euler.y = model_xy[1]
			r = random.sample(set([0,1,2,3]),1)[0]
			if (r == 0):
				model.rotation_euler.x = 0.0
				model.keyframe_insert(data_path="rotation_euler", index=-1)
				model.rotation_euler.y = 0.0
				model.keyframe_insert(data_path="rotation_euler", index=-1)
				model.location.z = 0.2425098
				model.keyframe_insert(data_path="location", index=-1)
			else:
				if (r == 1):
					model.rotation_euler.x = 1.57079637050628660
					model.keyframe_insert(data_path="rotation_euler", index=-1)
					model.rotation_euler.y = 0.0
					model.keyframe_insert(data_path="rotation_euler", index=-1)
					model.location.z = 0.1881001
					model.keyframe_insert(data_path="location", index=-1)
				else:
					if (r == 2):
						model.rotation_euler.x = 3.1415927410125732
						model.keyframe_insert(data_path="rotation_euler", index=-1)
						model.rotation_euler.y = 0.0
						model.keyframe_insert(data_path="rotation_euler", index=-1)
						model.location.z = 0.2425098
						model.keyframe_insert(data_path="location", index=-1)
					else:
						if (r == 3):
							model.rotation_euler.x = 4.71238899230957
							model.keyframe_insert(data_path="rotation_euler", index=-1)
							model.rotation_euler.y = 0.0
							model.keyframe_insert(data_path="rotation_euler", index=-1)
							model.location.z = 0.1881001
							model.keyframe_insert(data_path="location", index=-1)
			model.keyframe_insert(data_path="rotation_euler", index=-1)
			_cam1.location = cam_loc[num_rots]
			_cam1.keyframe_insert(data_path="location", index=-1)
			empty.rotation_euler.x = empt_rot[num_rots]
			empty.keyframe_insert(data_path="rotation_euler", index=-1)
			pointsCheck(fr,path_txt,_camtxt1,_imgtxt1,_imgworld,_mod,r)
			num_rots += 1
			fr += 1
	_camtxt1.close()
	_keytxt.close()
	_imgtxt1.close()
	_imgworld.close() 
	_mod.close()


# -------------------------------------------------animation launch------------------------------------------
def set_keys(keys_num,path_for_txt_files):
	bpy.data.scenes["Scene"].frame_end = keys_num
	model_cam_animation_render(keys_num, path_for_txt_files)
	logging.warning(" Model and camera animation is ready")
	bpy.ops.wm.save_mainfile()
	logging.warning(" Main file is saved")
	logging.warning(" All keys are set, master")



# -----------------------------------------parsing args-----------------------------------------------------
logging.warning(" Script is installed, I guess")
# def get_args():
# 	parser = argparse.ArgumentParser()
# 	_, all_arguments = parser.parse_known_args()
# 	double_dash_index = all_arguments.index('--')
# 	script_args = all_arguments[double_dash_index + 1: ]
# 	parser.add_argument('-t', '--pthtxt', help="path to information about camera and key points locations")
# 	parser.add_argument('-k', '--keys', help="number of key frames for one animation")
# 	parsed_script_args, _ = parser.parse_known_args(script_args)
# 	return parsed_script_args
	
# args = get_args()
# _pathtxt = args.pthtxt
# _keys = int(args.keys)
set_keys(100, "/Users/nats/Desktop/_GLOBAL_SCENE/render_21.03/")
