#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version:  1.0
@author:   Jianzhang Zhang, <jianzhang.zhang@foxmail.com>
@file:     synonymyprocess.py
@time:     2016-10-06
@function: 常用的文件操作方法
"""

import os
import json
def mkdir(path):
	"""
	path 写法：file = "G:\\xxoo\\test"
	:param path:
	:return:
	"""
	folder = os.path.exists(path)
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
	else:
		print('---this folder is exist!----')

def getFileList(dir, fileList=[]):
	"""
	遍历一个目录,输出所有文件名
	param dir: 待遍历的文件夹
	param filrList : 保存文件名的列表
	return fileList: 文件名列表
	"""
	newDir = dir
	if os.path.isfile(dir):
		fileList.append(dir)
	elif os.path.isdir(dir):
		for s in os.listdir(dir):
			# 如果需要忽略某些文件夹，使用以下代码
			# if s == "xxx":
			# continue
			newDir = os.path.join(dir, s)
			getFileList(newDir, fileList)
	return fileList


def readStrFromFile(filePath):
	"""
	从文件中读取字符串str
	param filePath: 文件路径
	return string : 文本字符串
	"""
	with open(filePath, "rb") as f:
		string = f.read()
	return string


def readLinesFromFile(filePath):
	"""
	从文件中读取字符串列表list
	param filePath: 文件路径
	return lines  : 文本字符串列表
	"""
	with open(filePath, "rb") as f:
		lines = f.readlines()
	return lines

def readJsonFile(filePath):
	"""
	使用：
	for key in dicts.keys():
		print(key)
	for valu in dicts.values():
		print(valu.values())
	:param filePath:
	:return:
	"""
	fb = open(filePath, 'r')
	dictsobj = json.load(fb)
	fb.close()
	return dictsobj
def appendDictRecordToFile(filepath,appenddicts):
	try:
		fb = open(filepath, 'r')
		dicts = json.load(fb)
		fb.close()
		dicts={**dicts,**appenddicts}
		jsondata = json.dumps(dicts,separators=(',', ':'))
	except:
		jsondata = json.dumps(appenddicts,separators=(',', ':'))
	with open(filepath, 'w') as fw:
		fw.write(jsondata)
		fw.close()
def writeStrToFile(filePath, string):
	"""
	将字符串写入文件中
	param filePath: 文件路径
	param string  : 字符串str
	"""
	with open(filePath, "wb") as f:
		f.write(string)
	f.close()

def appendStrToFile(filePath, string):
	"""
	将字符串追加写入文件中
	param filePath: 文件路径
	param string  : 字符串str
	"""
	with open(filePath, "a") as f:
		f.write(string)
	f.close()


def dumpToFile(filePath, content):
	"""
	将数据类型序列化存入本地文件
	param filePath: 文件路径
	param content : 待保存的内容(list, dict, tuple, ...)
	"""
	import pickle
	with open(filePath, "wb") as f:
		pickle.dump(content, f)


def loadFromFile(filePath):
	"""
	从本地文件中加载序列化的内容
	param filePath: 文件路径
	return content: 序列化保存的内容(e.g. list, dict, tuple, ...)
	"""
	import pickle
	with open(filePath) as f:
		content = pickle.load(f)
	return content
