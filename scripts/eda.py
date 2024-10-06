import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class EDA:
    def __init__(self, filepath):
        """Initializes the EDA class with the file path."""
        self.filepath = filepath
        self.data = None

    def load_data(self):
        """Loads the data from the specified CSV file."""
        try:
            self.data = pd.read_csv(self.filepath)
            print(f"Data loaded successfully from {self.filepath}")
            return self.data
        except FileNotFoundError as e:
            print(f"Error loading data: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def summarize_data(self):
        """Provides an overview of the dataset, including descriptive statistics and general information."""
        if self.data is not None:
            print("\nDataset Overview")
            print("-" * 30)
            print(f"Shape of the dataset: {self.data.shape}")
            print(f"\nSummary Statistics:\n{self.data.describe()}")
            print("\nGeneral Info:")
            self.data.info()
        else:
            print("Data not loaded yet. Please load the data first.")
    
    def plot_distributions(self):
        """Plots the distribution of all numerical features."""
        if self.data is not None:
            num_cols = self.data.select_dtypes(include='number').columns
            if not num_cols.empty:
                print("\nPlotting distributions for numerical features...")
                self.data[num_cols].hist(figsize=(12, 10), bins=20)
                plt.tight_layout()
                plt.show()
            else:
                print("No numerical columns found for plotting distributions.")
        else:
            print("Data not loaded yet. Please load the data first.")
    

    def plot_categorical_distributions(self, max_categories=20):
        """Plots the distribution of categorical features in batch mode for better performance.
        
        Args:
            max_categories (int): Maximum number of categories to display per feature.
        """
        if self.data is not None:
            # Select only the categorical columns (excluding dropped columns)
            self.data.drop(columns=["TransactionId", "CurrencyCode"], inplace=True, errors="ignore")
            cat_cols = self.data.select_dtypes(include='object').columns

            if not cat_cols.empty:
                print("\nPlotting distributions for categorical features...")
                
                # Determine the number of rows and columns for subplots
                n_cols = 2  # Number of plots per row
                n_rows = (len(cat_cols) + 1) // n_cols  # Calculate rows based on number of categorical columns

                fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))
                axes = axes.flatten()  # Flatten axes to handle both rows and columns dynamically

                for i, col in enumerate(cat_cols):
                    ax = axes[i]
                    # Get value counts, limiting to top categories if necessary
                    value_counts = self.data[col].value_counts().nlargest(max_categories)

                    sns.countplot(x=self.data[col], order=value_counts.index, ax=ax, palette="Set2", hue=self.data[col], legend=False)

                    
                    # sns.countplot(x=self.data[col],order=value_counts.index, ax=ax, palette="Set2", hue=None,legend=False)
                    ax.set_title(f'Distribution of {col}')
                    
                    # Set ticks and tick labels for better handling
                    ax.set_xticks(range(len(value_counts)))
                    ax.set_xticklabels(value_counts.index, rotation=45, ha='right')

                # Hide any unused axes
                for j in range(i + 1, len(axes)):
                    fig.delaxes(axes[j])

                plt.tight_layout()
                plt.show()
            else:
                print("No categorical columns found for plotting distributions.")
        else:
            print("Data not loaded yet. Please load the data first.")


    def correlation_matrix(self):
        """Displays the correlation matrix for numerical features."""
        if self.data is not None:
            num_data = self.data.select_dtypes(include='number')
            if not num_data.empty:
                print("\nDisplaying correlation matrix for numerical features...")
                plt.figure(figsize=(12, 10))
                sns.heatmap(num_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", square=True)
                plt.title("Correlation Matrix")
                plt.show()
            else:
                print("No numerical data available for correlation analysis.")
        else:
            print("Data not loaded yet. Please load the data first.")

    def detect_missing_values(self):
        """Checks for missing values and returns their count per feature."""
        if self.data is not None:
            print("\nChecking for missing values...")
            missing_values = self.data.isnull().sum()
            missing = missing_values[missing_values > 0]
            if not missing.empty:
                print(f"Missing values found:\n{missing}")
            else:
                print("No missing values detected.")
        else:
            print("Data not loaded yet. Please load the data first.")



    def plot_outliers_boxplots(self, columns=None):
        """Displays boxplots for the specified numerical columns, customized for outlier detection."""
        if self.data is not None:
            if columns is None:
                columns = self.data.select_dtypes(include='number').columns  # Default to all numeric columns
                
            # Ensure columns is a list and filter out any columns that are not in the data
            columns = [col for col in columns if col in self.data.columns]
            
            # Check if there are columns to plot
            if len(columns) > 0:
                print("\nPlotting boxplots for specified columns to detect outliers...")
                for col in columns:
                    plt.figure(figsize=(10, 6))
                    sns.boxplot(x=self.data[col], palette="Set2",hue=self.data[col], boxprops=dict(facecolor='lightgreen'), legend=False)
                    plt.title(f'Boxplot of {col} (Outlier Detection)')
                    plt.tight_layout()
                    plt.show()
            else:
                print("No valid numerical columns found for plotting.")
        else:
            print("Data not loaded yet. Please load the data first.")
