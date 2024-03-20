import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the dataset
def read_dataset(file_path):
    return pd.read_csv(file_path)

# Step 2: Perform statistical calculations
def analyze_grades(data):
    # Calculate statistics
    mean_grade = data['Grade'].mean()
    median_grade = data['Grade'].median()
    mode_grade = data['Grade'].mode()[0]
    std_dev_grade = data['Grade'].std()
    
    # Print statistics
    print("Mean Grade:", mean_grade)
    print("Median Grade:", median_grade)
    print("Mode Grade:", mode_grade)
    print("Standard Deviation of Grades:", std_dev_grade)

# Step 3: Visualize the data
def visualize_grades(data):
    # Histogram of grades
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Grade'], bins=10, kde=True, color='skyblue')
    plt.title('Distribution of Grades')
    plt.xlabel('Grade')
    plt.ylabel('Frequency')
    plt.savefig('grade_distribution.png')
    plt.show()

    # Box plot of grades
    plt.figure(figsize=(8, 6))
    sns.boxplot(data['Grade'], color='lightgreen')
    plt.title('Box Plot of Grades')
    plt.xlabel('Grade')
    plt.savefig('grade_boxplot.png')
    plt.show()

# Main function
if __name__ == "__main__":
    file_path = "/path/to/your/student/grades/dataset.csv"
    
    # Step 1: Read the dataset
    grades_data = read_dataset(file_path)
    
    # Step 2: Analyze grades
    analyze_grades(grades_data)
    
    # Step 3: Visualize grades
    visualize_grades(grades_data)
