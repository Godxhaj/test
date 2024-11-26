import os
from PIL import Image
import argparse

def resize_image(input_path, output_path, width, height):
    """
    Resizes an image to the specified width and height.
    """
    try:
        # Open the image
        image = Image.open(input_path)

        # Resize the image
        resized_image = image.resize((width, height))

        # Save the resized image
        resized_image.save(output_path)
        print(f"Image resized successfully: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Resize an image to specified dimensions.")
    parser.add_argument("input", help="Path to the input image file.")
    parser.add_argument("output", help="Path to save the resized image.")
    parser.add_argument("width", type=int, help="Width of the resized image.")
    parser.add_argument("height", type=int, help="Height of the resized image.")
    
    args = parser.parse_args()

    # Validate file paths
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' does not exist.")
        return
    
    # Resize the image
    resize_image(args.input, args.output, args.width, args.height)

if __name__ == "__main__":
    main()
