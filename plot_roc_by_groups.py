### ROC Comparison
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def plot_roc_groups(y_test, y_test_scores, group_test):
    # Compute ROC curve and ROC area for each class
    fpr, tpr, _ = roc_curve(y_test[:], y_test_scores[:])
    roc_auc = auc(fpr, tpr)

    # Compute ROC curve and ROC area for each class
    fpr_w, tpr_w, _ = roc_curve(y_test[(group_test=='black')], y_test_scores[(group_test=='black')])
    roc_auc_w = auc(fpr_w, tpr_w)

    fpr_m, tpr_m, _ = roc_curve(y_test[(group_test=='white')], y_test_scores[(group_test=='white')])
    roc_auc_m = auc(fpr_m, tpr_m)

    plt.figure()
    lw = 2
    plt.plot(fpr,tpr,color="darkorange",lw=lw,
        label="ROC curve All (area = %0.2f)" % roc_auc)

    plt.plot(fpr_w,tpr_w,color="green",lw=lw,
        label="ROC curve Black (area = %0.2f)" % roc_auc_w)

    plt.plot(fpr_m,tpr_m,color="blue",lw=lw,
        label="ROC curve White (area = %0.2f)" % roc_auc_m)

    plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Receiver operating characteristic example")
    plt.legend(loc="lower right")
    plt.show()
    
    