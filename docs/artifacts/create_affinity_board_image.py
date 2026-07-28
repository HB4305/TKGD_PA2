import os
from PIL import Image, ImageDraw, ImageFont

def generate_affinity_diagram():
    # Canvas setup
    width = 1920
    height = 1200
    bg_color = (248, 249, 250) # Light FigJam canvas
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Draw grid dots
    grid_spacing = 30
    dot_color = (220, 224, 230)
    for x in range(0, width, grid_spacing):
        for y in range(0, height, grid_spacing):
            draw.ellipse([x-1, y-1, x+1, y+1], fill=dot_color)

    # Try loading fonts
    try:
        font_title = ImageFont.truetype("arial.ttf", 32)
        font_subtitle = ImageFont.truetype("arial.ttf", 18)
        font_cluster_header = ImageFont.truetype("arialbd.ttf", 20)
        font_card_title = ImageFont.truetype("arialbd.ttf", 15)
        font_card_body = ImageFont.truetype("arial.ttf", 13)
        font_tag = ImageFont.truetype("arialbd.ttf", 12)
    except:
        font_title = font_subtitle = font_cluster_header = font_card_title = font_card_body = font_tag = ImageFont.load_default()

    # Header
    draw.rectangle([0, 0, width, 100], fill=(30, 41, 59))
    draw.text((40, 22), "GROUP 06 — FREESTYLE CHESS MOBILE WEB", fill=(255, 255, 255), font=font_title)
    draw.text((40, 62), "Requirement 2: User Analysis — Visual Affinity Diagram (Digital Sticky Notes N01 - N16)", fill=(148, 163, 184), font=font_subtitle)

    # Legend
    legend_x = 1420
    legend_y = 35
    # Problem Legend
    draw.rectangle([legend_x, legend_y, legend_x+16, legend_y+16], fill=(254, 205, 211), outline=(225, 29, 72))
    draw.text((legend_x+24, legend_y), "Problem Notes", fill=(255, 255, 255), font=font_card_body)
    # Idea Legend
    draw.rectangle([legend_x+200, legend_y, legend_x+216, legend_y+16], fill=(186, 230, 253), outline=(2, 132, 199))
    draw.text((legend_x+224, legend_y), "Idea Notes", fill=(255, 255, 255), font=font_card_body)

    # Clusters Definition in 100% English
    clusters = [
        {
            "id": "CLUSTER A",
            "title": "Ergonomic Navigation & One-Handed Reachability",
            "color": (238, 242, 255),
            "border": (99, 102, 241),
            "x": 60, "y": 140, "w": 870, "h": 490,
            "notes": [
                {
                    "id": "N01", "type": "PROBLEM", "tag": "Survey Q12, P01-P05, P07, P08",
                    "text": "Mobile Hamburger menu is placed at top-left, making one-handed thumb interaction painful/annoying."
                },
                {
                    "id": "N02", "type": "PROBLEM", "tag": "Survey Q13 (43.1%)",
                    "text": "Users must stretch fingers, shift phone grip, shift the phone, or use two hands to tap navigation items."
                },
                {
                    "id": "N03", "type": "IDEA", "tag": "Brainstorm Solution",
                    "text": "Move primary navigation to a persistent Bottom Navigation Bar."
                },
                {
                    "id": "N04", "type": "IDEA", "tag": "Brainstorm, P05",
                    "text": "Provide a floating action button (FAB) or bottom-right drawer for one-handed reachability."
                }
            ]
        },
        {
            "id": "CLUSTER B",
            "title": "Homepage Onboarding & Value Proposition Clarity",
            "color": (254, 243, 199),
            "border": (217, 119, 6),
            "x": 990, "y": 140, "w": 870, "h": 490,
            "notes": [
                {
                    "id": "N05", "type": "PROBLEM", "tag": "Survey Q09 (73.6%), P03/P05/P08",
                    "text": "Homepage Hero section is cluttered with banners and lacks onboarding explaining Freestyle Chess format to new users."
                },
                {
                    "id": "N06", "type": "PROBLEM", "tag": "Survey Q10 (52.8%), P03/P05/P08",
                    "text": "New users feel disoriented and do not understand website purpose upon landing."
                },
                {
                    "id": "N07", "type": "IDEA", "tag": "Brainstorm Solution",
                    "text": "Redesign Hero section with a minimalist intro banner, clear onboarding text, and prominent CTA."
                },
                {
                    "id": "N08", "type": "IDEA", "tag": "Brainstorm Solution",
                    "text": "Add an interactive 'What is Freestyle Chess?' quick modal guide for newcomers."
                }
            ]
        },
        {
            "id": "CLUSTER C",
            "title": "Search, Filtering & Information Retrieval",
            "color": (240, 253, 244),
            "border": (22, 163, 74),
            "x": 60, "y": 660, "w": 870, "h": 490,
            "notes": [
                {
                    "id": "N09", "type": "PROBLEM", "tag": "Survey Q16 (72%), P02/P05/P06/P08",
                    "text": "Rating leaderboard is an infinite scroll list with no sticky search bar, causing repetitive scrolling."
                },
                {
                    "id": "N10", "type": "PROBLEM", "tag": "Survey Q19 (61.1%), P02/P04/P06/P07",
                    "text": "Users cannot search news/events by keywords and must browse long chronological lists."
                },
                {
                    "id": "N11", "type": "IDEA", "tag": "Brainstorm Solution",
                    "text": "Add a Sticky Search Bar fixed at top of long listing pages (Rating, News, Videos)."
                },
                {
                    "id": "N12", "type": "IDEA", "tag": "Brainstorm Solution",
                    "text": "Provide filter chips (by major event, date, rating range) and auto-suggest search queries."
                }
            ]
        },
        {
            "id": "CLUSTER D",
            "title": "Video Player Interactions & Feedback",
            "color": (253, 242, 248),
            "border": (219, 39, 119),
            "x": 990, "y": 660, "w": 870, "h": 490,
            "notes": [
                {
                    "id": "N13", "type": "PROBLEM", "tag": "Survey Q21 (52.8%), P02/P03/P05-P07/P09",
                    "text": "Video player lacks immediate visual feedback (loading spinner) when tapped, leading to rage clicks."
                },
                {
                    "id": "N14", "type": "PROBLEM", "tag": "Interview P09/P10 clips, P04/P05/P07",
                    "text": "Playing a new video does not pause the previous video, resulting in overlapping audio channels."
                },
                {
                    "id": "N15", "type": "IDEA", "tag": "Brainstorm, P04/P05/P07/P09",
                    "text": "Enforce a Single-Player audio/video model (playing new video automatically stops old video)."
                },
                {
                    "id": "N16", "type": "IDEA", "tag": "Brainstorm, P02/P03/P09",
                    "text": "Add skeleton loaders and loading spinners instantly upon tapping video play controls."
                }
            ]
        }
    ]

    for c in clusters:
        # Draw Cluster Container
        draw.rectangle([c["x"], c["y"], c["x"]+c["w"], c["y"]+c["h"]], fill=c["color"], outline=c["border"], width=2)
        
        # Draw Cluster Title Banner
        draw.rectangle([c["x"], c["y"], c["x"]+c["w"], c["y"]+45], fill=c["border"])
        draw.text((c["x"]+20, c["y"]+10), f"{c['id']}: {c['title']}", fill=(255, 255, 255), font=font_cluster_header)

        # Draw Notes inside Cluster (2x2 grid)
        note_positions = [
            (c["x"]+20, c["y"]+65),
            (c["x"]+445, c["y"]+65),
            (c["x"]+20, c["y"]+270),
            (c["x"]+445, c["y"]+270)
        ]

        for i, note in enumerate(c["notes"]):
            nx, ny = note_positions[i]
            nw, nh = 405, 195

            # Sticky Note styling based on type
            if note["type"] == "PROBLEM":
                card_bg = (254, 226, 226)    # Soft red/pink
                card_border = (239, 68, 68)   # Red border
                badge_bg = (220, 38, 38)     # Red badge
                badge_text = "PROBLEM NOTE"
            else:
                card_bg = (224, 242, 254)    # Soft blue
                card_border = (56, 189, 248)  # Light blue border
                badge_bg = (3, 105, 161)      # Dark blue badge
                badge_text = "IDEA NOTE"

            # Draw Sticky Note Shadow
            draw.rectangle([nx+4, ny+4, nx+nw+4, ny+nh+4], fill=(210, 215, 225))

            # Draw Sticky Note Body
            draw.rectangle([nx, ny, nx+nw, ny+nh], fill=card_bg, outline=card_border, width=2)

            # Note ID & Badge Header
            draw.rectangle([nx+12, ny+12, nx+70, ny+32], fill=(15, 23, 42))
            draw.text((nx+20, ny+14), note["id"], fill=(255, 255, 255), font=font_card_title)

            draw.rectangle([nx+78, ny+12, nx+185, ny+32], fill=badge_bg)
            draw.text((nx+85, ny+15), badge_text, fill=(255, 255, 255), font=font_tag)

            # Tag / Evidence Line
            draw.text((nx+12, ny+40), f"Evidence: {note['tag']}", fill=(71, 85, 105), font=font_tag)

            # Draw Separator
            draw.line([nx+12, ny+58, nx+nw-12, ny+58], fill=card_border, width=1)

            # Wrap and Draw Text
            words = note["text"].split()
            lines = []
            current_line = ""
            for w in words:
                test_line = f"{current_line} {w}".strip()
                if len(test_line) > 44:
                    lines.append(current_line)
                    current_line = w
                else:
                    current_line = test_line
            if current_line:
                lines.append(current_line)

            text_y = ny + 68
            for line in lines:
                draw.text((nx+12, text_y), line, fill=(15, 23, 42), font=font_card_body)
                text_y += 20

    # Footer
    draw.text((width - 450, height - 30), "Generated for PA2 Group 06 Submission — FigJam Export Format", fill=(100, 116, 139), font=font_tag)

    # Save output
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "affinity_diagram.png")
    img.save(output_path, "PNG")
    print(f"Successfully generated English Affinity Diagram image at: {output_path}".encode("ascii", "ignore").decode("ascii"))

if __name__ == "__main__":
    generate_affinity_diagram()
