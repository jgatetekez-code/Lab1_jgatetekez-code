#!/bin/bash

archive_dir="archive"
log_file="organizer.log"
source_file="grades.csv"
log_timestamp=$(date +"%Y-%m-%d %H:%M:%S")
timestamp=$(date +"%Y%m%d-%H%M%S")
archived_file="grades_${timestamp}.csv"

if [ ! -d "$archive_dir" ]; then
    echo "Creating archive directory..."
    mkdir -p "$archive_dir"
fi

if [ -f "$source_file" ]; then
    echo "Archiving the grades.csv ..."
    mv "$source_file" "$archive_dir/$archived_file"
    echo "$log_timestamp | original: $source_file | archived: $archive_dir/$archived_file" >> "$log_file"

    echo "Created a new empty grades.csv"
    touch "$source_file"
else
    echo "grades.csv file was missing. Create a new one instead"
    touch "$source_file"
    echo "$log_timestamp | original: $source_file | archived: none (file did not exist)" >> "$log_file"
fi
