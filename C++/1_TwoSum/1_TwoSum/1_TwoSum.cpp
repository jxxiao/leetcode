// 1_TwoSum.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<int> twoSum(vector<int>&, int);

int main()
{
	vector<int> nums = { 0,2,4,0 };
	cout << twoSum(nums, 0)[0] << " " << twoSum(nums, 0)[1];
    return 0;
}


vector<int> twoSum(vector<int>& nums, int target) {
	vector<int> res;
	multimap<int, int> numsMap;
	multimap<int, int>::iterator iter;
	int max = nums.size();

	for (int i = 0; i < max; i++)
	{
		numsMap.insert(pair<int, int>(nums[i], i + 1));
	}
	for (iter = numsMap.begin(); iter != numsMap.end(); iter++)
	{
		if ((numsMap.end() != numsMap.find(target - iter->first)) &&
			((numsMap.find(target - iter->first))->second)
			!= iter->second)
		{
			res.push_back((iter->second));
			res.push_back((((numsMap.find(target - iter->first))->second)));
			sort(res.begin(), res.end());
			break;
		}
	}

	return res;
}


