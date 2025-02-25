# Use a specific version of the Rocker tidyverse image
FROM rocker/tidyverse:4.3.0

# Install additional system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    libharfbuzz-dev \
    libfribidi-dev \
    libtiff-dev \
    && rm -rf /var/lib/apt/lists/*

# Install additional R packages
RUN R -e "install.packages(c('bigrquery', 'DBI', 'grf', 'knitr', 'readr'))"

# Copy the R script into the container
COPY example.R /example.R

# Set the R script as the entrypoint with positional arguments
ENTRYPOINT ["Rscript", "/example.R"]