# Load the tidyverse package
library(tidyverse)

# Create a simple data frame
data <- tibble(
  x = 1:10,
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
  labs(title = "Test Plot: y = x^2", x = "X", y = "Y")

# Save the plot to a file
ggsave("test_plot.png", plot)

print("Plot saved as 'test_plot.png'")