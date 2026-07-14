from dataclasses import dataclass


@dataclass(frozen=True)
class ThresholdRule:
    feature_name: str
    feature_index: int
    threshold: float
    left_label: int
    right_label: int

    def predict(self, sample):
        if sample[self.feature_index] >= self.threshold:
            return self.right_label
        return self.left_label


def majority_vote(predictions):
    ones = sum(predictions)
    zeros = len(predictions) - ones
    if ones >= zeros:
        return 1
    return 0


sample = [0.8, 0.6, 1.0]

single_tree = ThresholdRule(
    feature_name="亮度",
    feature_index=0,
    threshold=0.5,
    left_label=0,
    right_label=1,
)

forest = [
    ThresholdRule("亮度", 0, 0.5, 0, 1),
    ThresholdRule("圆润程度", 1, 0.5, 0, 1),
    ThresholdRule("笔画像素数", 2, 1.5, 0, 1),
]

tree_prediction = single_tree.predict(sample)
forest_votes = [tree.predict(sample) for tree in forest]
forest_prediction = majority_vote(forest_votes)

print(f"样本特征：[亮度={sample[0]}, 圆润程度={sample[1]}, 笔画像素数={sample[2]}]")
print(f"单棵决策树规则：{single_tree.feature_name} >= {single_tree.threshold} 时预测 1")
print(f"单棵决策树预测：{tree_prediction}")
print(f"投票明细：{forest_votes}")
print(f"随机森林投票结果：{forest_prediction}")

if tree_prediction != 1:
    raise RuntimeError("单棵决策树预测不符合预期。")

if forest_votes != [1, 1, 0]:
    raise RuntimeError("随机森林投票明细不符合预期。")

if forest_prediction != 1:
    raise RuntimeError("随机森林投票结果不符合预期。")

print("决策树和随机森林验证通过")
