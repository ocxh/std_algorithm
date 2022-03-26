#pragma once

#ifndef __BINARY_TREE_H__
#define __BINARY_TREE_H__

typedef int BTData;

//노드 구조체
typedef struct _bTreeNode
{
	BTData data;
	struct _bTreeNode* left;
	struct _bTreeNode* right;
} BTreeNode;

//노드 생성
BTreeNode* MakeBTreeNode(void);
//노드 데이터 가져오기
BTData GETDATA(BTreeNode* bt);
//노드 데이터 설정
void SetData(BTreeNode* bt, BTData data);

//서브트리 가져오기
BTreeNode* GetLeftSubTree(BTreeNode* bt);
BTreeNode* GetRightSubTree(BTreeNode* bt);

//서브트리 생성
void MakeLeftSubTree(BTreeNode* main, BTreeNode* sub);
void MakeRightSubTree(BTreeNode* main, BTreeNode* sub);

//방문처리 함수 포인터
typedef void (*VisitFuncPtr)(BTData data);
//노드 순회
void PreorderTraverse(BTreeNode* bt, VisitFuncPtr action); //전위 순회
void InorderTraverse(BTreeNode* bt, VisitFuncPtr action); //중위 순회
void PostorderTraverse(BTreeNode* bt, VisitFuncPtr action); //후위 순회

//노드 소멸
void DeleteTree(BTreeNode* bt);

#endif