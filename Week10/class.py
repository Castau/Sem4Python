from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

P = np.array([[6, 5, 3, 1],
              [3, 6, 2, 2],
              [3, 4, 3, 1]])
Q = np.array([[1.50,  1.00],
              [2.00,  2.50],
              [5.00,  4.50],
              [16.00, 17.00]])
R = P.dot(Q)
# print(R)

shoppers = {
    'Paula': {'Is': 4, 'Juice': 2, 'Kakao': 3, 'Lagkager': 2},
    'Peter': {'Is': 2, 'Juice': 5, 'Kakao': 0, 'Lagkager': 4},
    'Pandora': {'Is': 5, 'Juice': 3, 'Kakao': 4, 'Lagkager': 5},
    'Pietro': {'Is': 1, 'Juice': 8, 'Kakao': 9, 'Lagkager': 1}
}
shop_prices = {
    'Netto': {'Is': 10.50, 'Juice': 2.25, 'Kakao': 4.50, 'Lagkager': 33.50},
    'Fakta': {'Is': 4.00, 'Juice': 4.50, 'Kakao': 6.25, 'Lagkager': 20.00}
}

shoppersM = pd.DataFrame(shoppers).T
# print(shoppersM.shape)
shopsM = pd.DataFrame(shop_prices)
res = shoppersM.dot(shopsM)

print(res)


corpus = [open(r"moby_dick.txt", encoding="utf-8").read()]
vectorizer = CountVectorizer()

fit = vectorizer.fit_transform(corpus)
print(type(fit))
result = fit.todense()
document_idx = vectorizer.vocabulary_["wood"]
document_count = sum(result[:, document_idx])
print("document occurs {} times in the text".format(document_count))
