import bpy
import random
import math
from random import uniform
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
import logging
import argparse

scene = bpy.context.scene

_keytxt = open("/Users/nats/Desktop/_GLOBAL_SCENE/render_22.03/keys.txt","w")
# _keytxt2 = open("/Users/nats/Desktop/_GLOBAL_SCENE/render_20.03/keys_new_locA.txt","w")
_camrottxt = open("/Users/nats/Desktop/_GLOBAL_SCENE/render_20.03/cam_rot.txt","w")

fr = 0

for x in range(0,25):
	scene.frame_set(fr)
	cam1 = bpy.data.objects["Camera"]
	rotmode = cam1.rotation_mode
	order = rotmode if rotmode not in {'QUATERNION', 'AXIS_ANGLE'} else 'XYZ'
	rot_euler = cam1.matrix_world.to_euler(order)
	rot_x = rot_euler[0]
	rot_z = rot_euler[2]
	locCam1 = Vector((cam1.matrix_world[0][3],cam1.matrix_world[1][3],cam1.matrix_world[2][3]))
	ka = bpy.context.scene.objects['K.000']
	kb = bpy.context.scene.objects['K.001']
	kc = bpy.context.scene.objects['K.002']
	kd = bpy.context.scene.objects['K.003']
	ke = bpy.context.scene.objects['K.004']
	kf = bpy.context.scene.objects['K.005']
	kg = bpy.context.scene.objects['K.006']
	kh = bpy.context.scene.objects['K.007']
	ki = bpy.context.scene.objects['K.008']
	kj = bpy.context.scene.objects['K.009']
	kk = bpy.context.scene.objects['K.010']
	kl = bpy.context.scene.objects['K.011']
	km = bpy.context.scene.objects['K.012']
	kn = bpy.context.scene.objects['K.013']
	ko = bpy.context.scene.objects['K.014']
	kp = bpy.context.scene.objects['K.015']
	kq = bpy.context.scene.objects['K.016']
	kr = bpy.context.scene.objects['K.017']
	ks = bpy.context.scene.objects['K.018']
	kt = bpy.context.scene.objects['K.019']
	ku = bpy.context.scene.objects['K.020']
	kv = bpy.context.scene.objects['K.021']
	kw = bpy.context.scene.objects['K.022']
	kx = bpy.context.scene.objects['K.023']
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
	# locations = (locA,locB,locC,locD,locE,locF,locG,locH,locI,locJ,locK, locL,locM,locN,locO,locP,locQ,locR,locS,locT,locU,locV,locW,locX)
	_keytxt.write('%05d.png' % x + ", ")
	# for l in locations:
	# 	kp.matrix_world[0][3] = l[0]
	# 	kp.matrix_world[1][3] = l[1]
	# 	kp.matrix_world[2][3] = l[2]
	# 	# keytxt.write(str(kp.location.x) + ", " + str(kp.location.y) + ", " + str(kp.location.z) + "; ")
	# 	_keytxt.write(str(kp.matrix_world[0][3]) + ", " + str(kp.matrix_world[1][3]) + ", " + str(kp.matrix_world[2][3]) + "; ")
	# _keytxt.write("\n")
	_camrottxt.write('%05d.png' % x + ", " + str(rot_x) + ", " + str(rot_z) + "\n")
	ka.matrix_world[0][3] = locA[0]
	ka.matrix_world[1][3] = locA[1]
	ka.matrix_world[2][3] = locA[2]
	ka.keyframe_insert(data_path="location", index=-1)
	# _keytxt2.write(str(locA[0]) + ", " + str(locA[1]) + ", " + str(locA[2]) + "; ")
	_keytxt.write(str(ka.location.x) + ", " + str(ka.location.y) + ", " + str(ka.location.z) + "; ")
	kb.matrix_world[0][3] = locB[0]
	kb.matrix_world[1][3] = locB[1]
	kb.matrix_world[2][3] = locB[2]
	kb.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kb.location.x) + ", " + str(kb.location.y) + ", " + str(kb.location.z) + "; ")
	kc.matrix_world[0][3] = locC[0]
	kc.matrix_world[1][3] = locC[1]
	kc.matrix_world[2][3] = locC[2]
	kc.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kc.location.x) + ", " + str(kc.location.y) + ", " + str(kc.location.z) + "; ")
	kd.matrix_world[0][3] = locD[0]
	kd.matrix_world[1][3] = locD[1]
	kd.matrix_world[2][3] = locD[2]
	kd.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kd.location.x) + ", " + str(kd.location.y) + ", " + str(kd.location.z) + "; ")
	ke.matrix_world[0][3] = locE[0]
	ke.matrix_world[1][3] = locE[1]
	ke.matrix_world[2][3] = locE[2]
	ke.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(ke.location.x) + ", " + str(ke.location.y) + ", " + str(ke.location.z) + "; ")
	kf.matrix_world[0][3] = locF[0]
	kf.matrix_world[1][3] = locF[1]
	kf.matrix_world[2][3] = locF[2]
	kf.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kf.location.x) + ", " + str(kf.location.y) + ", " + str(kf.location.z) + "; ")
	kg.matrix_world[0][3] = locG[0]
	kg.matrix_world[1][3] = locG[1]
	kg.matrix_world[2][3] = locG[2]
	kg.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kg.location.x) + ", " + str(kg.location.y) + ", " + str(kg.location.z) + "; ")
	kh.matrix_world[0][3] = locH[0]
	kh.matrix_world[1][3] = locH[1]
	kh.matrix_world[2][3] = locH[2]
	kh.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kh.location.x) + ", " + str(kh.location.y) + ", " + str(kh.location.z) + "; ")
	ki.matrix_world[0][3] = locI[0]
	ki.matrix_world[1][3] = locI[1]
	ki.matrix_world[2][3] = locI[2]
	ki.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(ki.location.x) + ", " + str(ki.location.y) + ", " + str(ki.location.z) + "; ")
	kj.matrix_world[0][3] = locJ[0]
	kj.matrix_world[1][3] = locJ[1]
	kj.matrix_world[2][3] = locJ[2]
	kj.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kj.location.x) + ", " + str(kj.location.y) + ", " + str(kj.location.z) + "; ")
	kk.matrix_world[0][3] = locK[0]
	kk.matrix_world[1][3] = locK[1]
	kk.matrix_world[2][3] = locK[2]
	kk.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kk.location.x) + ", " + str(kk.location.y) + ", " + str(kk.location.z) + "; ")
	kl.matrix_world[0][3] = locL[0]
	kl.matrix_world[1][3] = locL[1]
	kl.matrix_world[2][3] = locL[2]
	kl.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kl.location.x) + ", " + str(kl.location.y) + ", " + str(kl.location.z) + "; ")
	km.matrix_world[0][3] = locM[0]
	km.matrix_world[1][3] = locM[1]
	km.matrix_world[2][3] = locM[2]
	km.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(km.location.x) + ", " + str(km.location.y) + ", " + str(km.location.z) + "; ")
	kn.matrix_world[0][3] = locN[0]
	kn.matrix_world[1][3] = locN[1]
	kn.matrix_world[2][3] = locN[2]
	kn.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kn.location.x) + ", " + str(kn.location.y) + ", " + str(kn.location.z) + "; ")
	ko.matrix_world[0][3] = locO[0]
	ko.matrix_world[1][3] = locO[1]
	ko.matrix_world[2][3] = locO[2]
	ko.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(ko.location.x) + ", " + str(ko.location.y) + ", " + str(ko.location.z) + "; ")
	kp.matrix_world[0][3] = locP[0]
	kp.matrix_world[1][3] = locP[1]
	kp.matrix_world[2][3] = locP[2]
	kp.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kp.location.x) + ", " + str(kp.location.y) + ", " + str(kp.location.z) + "; ")
	kq.matrix_world[0][3] = locQ[0]
	kq.matrix_world[1][3] = locQ[1]
	kq.matrix_world[2][3] = locQ[2]
	kq.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kq.location.x) + ", " + str(kq.location.y) + ", " + str(kq.location.z) + "; ")
	kr.matrix_world[0][3] = locR[0]
	kr.matrix_world[1][3] = locR[1]
	kr.matrix_world[2][3] = locR[2]
	kr.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kr.location.x) + ", " + str(kr.location.y) + ", " + str(kr.location.z) + "; ")
	ks.matrix_world[0][3] = locS[0]
	ks.matrix_world[1][3] = locS[1]
	ks.matrix_world[2][3] = locS[2]
	ks.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(ks.location.x) + ", " + str(ks.location.y) + ", " + str(ks.location.z) + "; ")
	kt.matrix_world[0][3] = locT[0]
	kt.matrix_world[1][3] = locT[1]
	kt.matrix_world[2][3] = locT[2]
	kt.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kt.location.x) + ", " + str(kt.location.y) + ", " + str(kt.location.z) + "; ")
	ku.matrix_world[0][3] = locU[0]
	ku.matrix_world[1][3] = locU[1]
	ku.matrix_world[2][3] = locU[2]
	ku.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(ku.location.x) + ", " + str(ku.location.y) + ", " + str(ku.location.z) + "; ")
	kv.matrix_world[0][3] = locV[0]
	kv.matrix_world[1][3] = locV[1]
	kv.matrix_world[2][3] = locV[2]
	kv.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kv.location.x) + ", " + str(kv.location.y) + ", " + str(kv.location.z) + "; ")
	kw.matrix_world[0][3] = locW[0]
	kw.matrix_world[1][3] = locW[1]
	kw.matrix_world[2][3] = locW[2]
	kw.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kw.location.x) + ", " + str(kw.location.y) + ", " + str(kw.location.z) + "; ")
	kx.matrix_world[0][3] = locX[0]
	kx.matrix_world[1][3] = locX[1]
	kx.matrix_world[2][3] = locX[2]
	kx.keyframe_insert(data_path="location", index=-1)
	_keytxt.write(str(kx.location.x) + ", " + str(kx.location.y) + ", " + str(kx.location.z) + "; ")
	_keytxt.write("\n")
	fr = fr + 1

_keytxt.close()
_camrottxt.close()