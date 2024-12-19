def parse_markdown_list(filename):
    ideas = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.readlines()
            
            for line in content:
                # Remove leading/trailing whitespace
                line = line.strip()
                
                # Check for list items (both - and * markers)
                if line.startswith('-') or line.startswith('*'):
                    # Remove the marker and any leading space
                    idea = line[1:].strip()
                    ideas.append(idea)
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error reading file: {e}")
        
    return ideas

# Example usage
if __name__ == "__main__":
    filename = "usecases/bokeh_usecases.md"
    ideas_list = parse_markdown_list(filename)
    
    # Print parsed ideas
    for i, idea in enumerate(ideas_list, 1):
        print(f"{i}. {idea}")
