#pragma once

#ifndef __BINARY_TREE_H__
#define __BINARY_TREE_H__

typedef int BTData;

//��� ����ü
typedef struct _bTreeNode
{
	BTData data;
	struct _bTreeNode* left;
	struct _bTreeNode* right;
} BTreeNode;

//��� ����
BTreeNode* MakeBTreeNode(void);
//��� ������ ��������
BTData GETDATA(BTreeNode* bt);
//��� ������ ����
void SetData(BTreeNode* bt, BTData data);

//����Ʈ�� ��������
BTreeNode* GetLeftSubTree(BTreeNode* bt);
BTreeNode* GetRightSubTree(BTreeNode* bt);

//����Ʈ�� ����
void MakeLeftSubTree(BTreeNode* main, BTreeNode* sub);
void MakeRightSubTree(BTreeNode* main, BTreeNode* sub);

//�湮ó�� �Լ� ������
typedef void (*VisitFuncPtr)(BTData data);
//��� ��ȸ
void PreorderTraverse(BTreeNode* bt, VisitFuncPtr action); //���� ��ȸ
void InorderTraverse(BTreeNode* bt, VisitFuncPtr action); //���� ��ȸ
void PostorderTraverse(BTreeNode* bt, VisitFuncPtr action); //���� ��ȸ

//��� �Ҹ�
void DeleteTree(BTreeNode* bt);

#endif