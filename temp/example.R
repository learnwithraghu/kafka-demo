# Load the tidyverse package
library(tidyverse)

# Read positional arguments
args <- commandArgs(trailingOnly = TRUE)

# Check if the correct number of arguments is provided
if (length(args) != 2) {
  stop("Please provide two arguments: the maximum value for x and the output plot filename.")
}

# Parse arguments
max_x <- as.numeric(args[1])  # First argument: maximum value for x
output_file <- args[2]        # Second argument: output plot filename

# Create a simple data frame
data <- tibble(
  x = 1:max_x,
  y = x^2
)

# Print the data frame
print("Original Data:")
print(data)

# Perform some basic data manipulation
data <- data %>%
  mutate(z = y / 2)

# Print the modified data frame
print("Modified Data:")
print(data)

# Create a simple plot
plot <- ggplot(data, aes(x = x, y = y)) +
  geom_line(color = "blue") +
  geom_point(size = 3, color = "red") +
  labs(title = paste("Test Plot: y = x^2 (1 to", max_x, ")"), x = "X", y = "Y")

# Save the plot to the specified file
ggsave(output_file, plot)

print(paste("Plot saved as", output_file))