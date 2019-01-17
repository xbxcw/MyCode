# coding=utf-8
import datetime
import json
import pprint
import shutil
from PIL import Image, ImageChops
import ast
from maya import cmds
import logging
import os
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm

from CommonTools import tools

JSONFILESPATH = r"D:\jsons"
PROJECTPATH = r'D:\testProject'
MAYAPROJECT = cmds.workspace(fn=True)


class IntmeCommodity(dict):
    def createPBS(self, name, direcotory=os.path.join(MAYAPROJECT, 'sourceimages')):
        if cmds.ls(sl=True, type='dagNode'):
            meshName = cmds.ls(sl=True, type='dagNode')[0]
        else:
            cmds.warning(u'未选择模型')
            return
        for i in os.listdir(MAYAPROJECT):
            if i.endswith('AmbientOcclusion.png'):
                # shutil.copyfile(os.path.join(MAYAPROJECT, i), os.path.join(direcotory, 'T_%s_ao.png' % name))
                im = Image.open(os.path.join(MAYAPROJECT, i))
                im = im.resize((512, 512), Image.ANTIALIAS)
                im.save(os.path.join(direcotory, 'T_%s_ao.png' % name))
                os.remove(os.path.join(MAYAPROJECT, i))
            if i.endswith('Diffuse.png'):
                # shutil.copyfile(os.path.join(MAYAPROJECT, i), os.path.join(direcotory, 'T_%s_b.png' % name))
                im = Image.open(os.path.join(MAYAPROJECT, i))
                im = im.resize((2048, 2048), Image.ANTIALIAS)
                im.save(os.path.join(direcotory, 'T_%s_b.png' % name))

                os.remove(os.path.join(MAYAPROJECT, i))

            if i.endswith('Normals.png'):
                # shutil.copyfile(os.path.join(MAYAPROJECT, i), os.path.join(direcotory, 'T_%s_n.png' % name))
                im = Image.open(os.path.join(MAYAPROJECT, i))
                im = im.resize((2048, 2048), Image.ANTIALIAS)
                im.save(os.path.join(direcotory, 'T_%s_n.png' % name))

                os.remove(os.path.join(MAYAPROJECT, i))

        shaderName = 'M_' + name + '_w'
        shader = cmds.shadingNode('StingrayPBS', asShader=True, name=shaderName)
        cmds.shaderfx(sfxnode=shader, initShaderAttributes=True)  # 初始化pbs

        shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderName + 'SG')
        cmds.connectAttr(shader + '.outColor', shading_group + '.surfaceShader')

        imges = os.listdir(direcotory)
        for img in imges:
            if img.endswith('%s_b.png' % name):
                baseTex = os.path.join(direcotory, img)
                baseColor = cmds.shadingNode('file', at=True, name='T_' + name + '_b')
                cmds.setAttr(shader + '.use_color_map', 1)
                cmds.connectAttr(baseColor + '.outColor', shader + '.TEX_color_map')
                cmds.setAttr(baseColor + '.fileTextureName', baseTex, type='string')

            if img.endswith('%s_n.png' % name):
                noramlTex = os.path.join(direcotory, img)
                normal = cmds.shadingNode('file', at=True, name='T_' + name + '_n')
                cmds.setAttr(shader + '.use_normal_map', 1)
                cmds.connectAttr(normal + '.outColor', shader + '.TEX_normal_map')
                cmds.setAttr(normal + '.fileTextureName', noramlTex, type='string')

            if img.endswith('%s_ao.png' % name):
                aoTex = os.path.join(direcotory, img)
                ambientOcclusion = cmds.shadingNode('file', at=True, name='T_' + name + '_ao')
                cmds.setAttr(shader + '.use_ao_map', 1)
                cmds.connectAttr(ambientOcclusion + '.outColor', shader + '.TEX_ao_map')
                cmds.setAttr(ambientOcclusion + '.fileTextureName', aoTex, type='string')

            if img.endswith('%s_r.png' % name):
                roughnessTex = os.path.join(direcotory, img)
                roughness = cmds.shadingNode('file', at=True, name='T_' + name + '_r')
                cmds.setAttr(shader + '.use_roughness_map', 1)
                cmds.connectAttr(roughness + '.outColor', shader + '.TEX_roughness_map')
                cmds.setAttr(roughness + '.fileTextureName', roughnessTex, type='string')

            if img.endswith('%s_m.png' % name):
                metallicTex = os.path.join(direcotory, img)
                metallic = cmds.shadingNode('file', at=True, name='T_' + name + '_m')
                cmds.setAttr(shader + '.use_metallic_map', 1)
                cmds.connectAttr(metallic + '.outColor', shader + '.TEX_metallic_map')
                cmds.setAttr(metallic + '.fileTextureName', metallicTex, type='string')

            if img.endswith('%s_e.png' % name):
                emissiveTex = os.path.join(direcotory, img)
                emissive = cmds.shadingNode('file', at=True, name='T_' + name + '_e')
                cmds.setAttr(shader + '.use_emissive_map', 1)
                cmds.connectAttr(emissive + '.outColor', shader + '.TEX_emissive_map')
                cmds.setAttr(emissive + '.fileTextureName', emissiveTex, type='string')

        # cmds.setAttr(ao + '.fileTextureName', i[0], type='string')
        cmds.sets(meshName, e=True, fe=shading_group)

    def createShadow(self, name, direcotory=os.path.join(MAYAPROJECT, 'sourceimages')):
        if cmds.ls(sl=True, type='dagNode'):
            meshName = cmds.ls(sl=True, type='dagNode')[0]
        else:
            cmds.warning(u'未选择模型')
            return

        if 'T_%s_s.png' % name in os.listdir(direcotory):
            shaderName = 'M_' + name + '_s'
            shader = cmds.shadingNode('lambert', asShader=True, name=shaderName)
            shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderName + 'SG')
            cmds.connectAttr(shader + '.outColor', shading_group + '.surfaceShader')
            shadowTex = os.path.join(direcotory, os.path.join(direcotory, 'T_%s_s.png' % name))
            shadow = cmds.shadingNode('file', at=True, name='T_' + name + '_s')
            cmds.connectAttr(shadow + '.outColor', shader + '.color')
            cmds.connectAttr(shadow + '.outTransparency', shader + '.transparency')

            cmds.setAttr(shadow + '.fileTextureName', shadowTex, type='string')
            cmds.sets(meshName, e=True, fe=shading_group)

        else:
            cmds.warning(u'没有影子贴图')
            return

    def findCommodity(self, directory=JSONFILESPATH):
        """
        找到文件夹下所有json，存入字典
        :param directory: json文件夹地址
        :return:
        """
        self.clear()
        files = os.listdir(directory)
        for file in files:
            name, ext = os.path.splitext(file)
            commodityInfo = os.path.join(directory, file)
            with open(commodityInfo, 'r') as f:
                info = json.load(f)

            self[name] = eval(json.dumps(info, encoding="utf-8", ensure_ascii=False))

    def loadMayaFile(self, name, versions):
        """
        从服务器上打开maya文件
        :param name: 文件名
        :param versions: 版本
        :return:
        """
        a = self[name][versions]['maya文件地址']['path']
        shutil.copy(a, os.path.join(MAYAPROJECT, 'scenes'))

        cmds.file(os.path.join(MAYAPROJECT, 'scenes/%s.ma' % name), o=True, force=True)

    def saveMayaFile(self, name):
        """
        保存本地maya
        :param name: 文件名
        :return:
        """
        maName = os.path.join(MAYAPROJECT, 'scenes//%s.ma' % name)
        cmds.file(rename=maName)
        cmds.file(save=True, type='mayaAscii', force=True)
        return maName

    def openMayaFile(self, name):
        '''
        打开maya文件
        :param name: 文件名
        :return:
        '''
        maName = os.path.join(cmds.workspace(fn=True), 'scenes//%s.ma' % name)
        cmds.file(maName, o=True, force=True)

    def updateMayaFile(self, name, directory=PROJECTPATH, note=''):
        """
        上传maya文件
        :param name: 名字
        :param directory: 项目地址
        :param note: 摘要
        :return:
        """
        date = datetime.date.today()
        nameDirectory = os.path.join(directory, name)
        tools.createDirectory(nameDirectory)
        dateDirectory = os.path.join(nameDirectory, '%s' % date)
        tools.createDirectory(dateDirectory)
        mayaDirectory = os.path.join(dateDirectory, 'maya')

        tools.createDirectory(mayaDirectory)
        shutil.copy(self.saveMayaFile(name), mayaDirectory)
        self[name]['%s' % date]['note'] = note
        self[name]['%s' % date]['maya文件地址'] = os.path.join(dateDirectory, '%s.ma' % name)
        with open(os.path.join(JSONFILESPATH, '%s.json' % name), 'w') as f:
            json.dump(self[name], f, ensure_ascii=False)


def run():
    name = []
    a = IntmeCommodity()
    a.findCommodity()
    for n, info in a.items():
        name.append(n)

    a.createShadow(name[0])

    # a.loadMayaFile(name=name[0], versions='2019-01-12')
def imges(imge=r"D:\HKW\mayacontroller\turtle\bakedTextures\baked_beauty_pPlaneShape1.png"):
    img = Image.open(imge)
    img = img.convert('L')
    img = ImageChops.invert(img)
    img1 = Image.new('RGBA',(512,512),(0,0,0,0))
    img1.putalpha(img)
    img1.save(r"D:\HKW\mayacontroller\turtle\bakedTextures\aa1.png")