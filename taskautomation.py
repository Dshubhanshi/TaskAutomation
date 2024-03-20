import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_dataset(file_path):
    return pd.read_csv(file_path)

def analyze_grades(data):
    mean_grade = data['Grade'].mean()
    median_grade = data['Grade'].median()
    mode_grade = data['Grade'].mode()[0]
    std_dev_grade = data['Grade'].std()
    
    print("Mean Grade:", mean_grade)
    print("Median Grade:", median_grade)
    print("Mode Grade:", mode_grade)
    print("Standard Deviation of Grades:", std_dev_grade)

def visualize_grades(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Grade'], bins=10, kde=True, color='skyblue')
    plt.title('Distribution of Grades')
    plt.xlabel('Grade')
    plt.ylabel('Frequency')
    plt.savefig('grade_distribution.png')
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.boxplot(data['Grade'], color='lightgreen')
    plt.title('Box Plot of Grades')
    plt.xlabel('Grade')
    plt.savefig('grade_boxplot.png')
    plt.show()

if __name__ == "__main__":
    file_path = "/path/to/your/student/grades/dataset.csv"
    
    grades_data = read_dataset(file_path)
    
    analyze_grades(grades_data)
    
    visualize_grades(grades_data)
