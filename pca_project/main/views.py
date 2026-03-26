from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("slide1")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


@login_required
def slide1(request):
    return render(request, "slide1.html")

@login_required
def slide2(request):
    return render(request, "slide2.html")

@login_required
def slide3(request):
    return render(request, "slide3.html")

@login_required
def slide4(request):
    return render(request, "slide4.html")

@login_required
def slide5(request):
    return render(request, "slide5.html")

@login_required
def slide6(request):
    return render(request, "slide6.html")

@login_required
def slide7(request):
    return render(request, "slide7.html")

@login_required
def slide8(request):
    return render(request, "slide8.html")

@login_required
def slide9(request):
    return render(request, "slide9.html")

@login_required
def slide10(request):
    return render(request, "slide10.html")





import matplotlib
matplotlib.use('Agg')   

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

from django.shortcuts import render
from django.conf import settings

# Plotly (for heatmap + zscore)
import plotly.express as px
import plotly.io as pio


def run_pca(request):

    # TAKE FILE FROM USER
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        data = pd.read_csv(csv_file)
    else:
        return render(request, 'slide2.html')

    # Fix encoding
    data.columns = data.columns.str.replace('ï»¿','', regex=True)

    # Remove duplicates
    data = data.drop_duplicates()

    # Remove constant columns
    for col in data.columns:
        if data[col].nunique() == 1:
            data = data.drop(columns=[col])

    # Select numeric data
    numeric_data = data.select_dtypes(include=[np.number])

    # HEATMAP 
    corr = numeric_data.corr()
    fig1 = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r')
    heatmap_html = pio.to_html(fig1, full_html=False)

    # COVARIANCE
    cov_matrix = numeric_data.cov().to_html()

    # Z-SCORE 
    z_scores = np.abs(zscore(numeric_data))
    fig2 = px.box(z_scores)
    zscore_html = pio.to_html(fig2, full_html=False)

    #  PCA
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(numeric_data)

    pca = PCA(n_components=4)
    X_pca = pca.fit_transform(X_scaled)

    # PCA dataframe
    pca_df = pd.DataFrame(X_pca, columns=["PC1", "PC2", "PC3", "PC4"])

    # Add label if exists
    if 'label' in data.columns:
        pca_df['Label'] = data['label']
    elif 'status' in data.columns:
        pca_df['Label'] = data['status']
    else:
        pca_df['Label'] = "Data"

    # PCA table
    pca_table = pca_df.head(20).to_html()

    #  MATPLOTLIB SCATTER 
    plt.figure(figsize=(6,4))

    sns.scatterplot(
        x="PC1",
        y="PC2",
        hue="Label",
        data=pca_df,
        palette="Set1"
    )

    plt.title("PCA Visualization (PC1 vs PC2)")
    plt.xlabel("PC1")
    plt.ylabel("PC2")

    # CREATE MEDIA FOLDER
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

    scatter_path = os.path.join(settings.MEDIA_ROOT, "pca_scatter.png")
    plt.savefig(scatter_path)
    plt.close()

    #  VARIANCE 
    variance = pca.explained_variance_ratio_
    variance_text = [f"PC{i+1}: {v*100:.2f}%" for i, v in enumerate(variance)]
    total_variance = f"{sum(variance)*100:.2f}%"

    # CONTEXT 
    context = {
        "cov_matrix": cov_matrix,
        "heatmap": heatmap_html,
        "zscore": zscore_html,
        "pca_table": pca_table,
        "pca_scatter": settings.MEDIA_URL + "pca_scatter.png",
        "variance": variance_text,
        "total_variance": total_variance
    }

    return render(request, "result.html", context)