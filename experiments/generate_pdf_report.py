def generate_pdf_report(results_dir, report_name, test_description=None):
    """
    Generate a consolidated PDF report containing all visualizations created by the test script.
    
    Args:
        results_dir: Directory containing the test results and images
        report_name: Name for the PDF report
        test_description: Optional description to include in the report
    """
    import os
    import glob
    import datetime
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    
    # Ensure the directory exists
    if not os.path.exists(results_dir):
        print(f"Results directory {results_dir} not found. Cannot generate report.")
        return
    
    # Define the report path
    report_path = os.path.join(results_dir, f"{report_name}.pdf")
    
    # Find all image files in the results directory
    image_files = []
    for ext in ['png', 'jpg', 'jpeg']:
        image_files.extend(glob.glob(os.path.join(results_dir, f"*.{ext}")))
    
    # Sort files by modification time to maintain logical order
    image_files.sort(key=os.path.getmtime)
    
    if not image_files:
        print(f"No image files found in {results_dir}. Cannot generate report.")
        return
    
    # Create PDF
    with PdfPages(report_path) as pdf:
        # Add a cover page with test information
        plt.figure(figsize=(8.5, 11))
        plt.axis('off')
        
        # Title and date information
        title_text = [
            f"# {report_name}",
            f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Test Directory: {os.path.basename(results_dir)}"
        ]
        
        # Add description if provided
        if test_description:
            title_text.append("\n## Test Description")
            title_text.append(test_description)
        
        # Add file list
        title_text.append("\n## Visualizations Included")
        for i, img_file in enumerate(image_files):
            title_text.append(f"{i+1}. {os.path.basename(img_file)}")
        
        # Display text
        plt.text(0.1, 0.5, '\n'.join(title_text), 
                 fontsize=12, va='center', ha='left',
                 transform=plt.gca().transAxes,
                 family='monospace')
        
        pdf.savefig()
        plt.close()
        
        # Add each image to the PDF
        for img_file in image_files:
            # Create a figure with the same size as the image
            img = plt.imread(img_file)
            height, width = img.shape[:2]
            dpi = 100
            figsize = (width/dpi, height/dpi)
            
            # Create figure and add the image
            plt.figure(figsize=figsize, dpi=dpi)
            plt.axis('off')
            plt.imshow(img)
            
            # Add caption with filename
            plt.figtext(0.5, 0.01, os.path.basename(img_file), 
                       ha='center', fontsize=8)
            
            # Save to PDF
            pdf.savefig()
            plt.close()
    
    print(f"PDF report generated: {report_path}")
    return report_path