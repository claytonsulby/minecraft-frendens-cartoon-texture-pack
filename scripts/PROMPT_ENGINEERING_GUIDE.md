# Image Prompt Engineering Guide for Minecraft Textures

This guide provides formulas and techniques for creating highly detailed, technical prompts that produce the exact textures you want.

## Universal Prompt Formula

```
[MEDIUM/STYLE] of [SUBJECT], [KEY CHARACTERISTICS], 
[COMPOSITION/FRAMING], [LIGHTING], [COLOR PALETTE], 
[MOOD/ATMOSPHERE], [TECHNICAL DETAILS]
```

## Detailed Component Breakdown

### 1. Medium/Style (How it should look)
**Options:**
- **Artistic Styles**: cartoon illustration, pixel art, watercolor painting, oil painting, pencil sketch, vector art, isometric art, voxel art
- **Photo Styles**: photorealistic, studio photograph, macro photography, product shot
- **Game Styles**: Minecraft-style, retro game sprite, 8-bit, 16-bit, low-poly 3D
- **Texture Styles**: hand-painted texture, procedural texture, PBR material, seamless tileable texture

**Examples:**
```
"Cartoon-style illustration"
"Hand-painted seamless texture"
"Photorealistic PBR material"
"Pixel art game sprite in 16x16 resolution"
```

### 2. Subject (What it is)
Be extremely specific about what the texture represents.

**Formula**: `[quantity] [material/object] [key features]`

**Examples:**
```
"A single dirt block face showing brown soil with scattered pebbles"
"A stack of oak wood planks with visible grain patterns"
"A diamond ore embedded in dark gray stone matrix"
```

### 3. Key Characteristics (Distinctive features)
List 3-5 specific visual features that define your texture.

**Categories:**
- **Surface**: rough, smooth, bumpy, cracked, weathered, pristine, glossy, matte
- **Patterns**: geometric, organic, repeating, random, scattered, clustered
- **Features**: pores, cracks, veins, crystals, fibers, grains, scratches
- **Scale**: fine-grained, coarse, chunky, delicate, bold

**Examples:**
```
"featuring visible wood grain, small knots, and subtle color variation"
"with angular geometric cracks and rough, uneven surface"
"showing crystalline structure with sharp facets and internal reflections"
```

### 4. Composition/Framing (Camera view)
Critical for game textures to specify how the texture fills the frame.

**Options:**
- `flat, straight-on view` — Standard for block faces
- `tileable seamless pattern` — Edges connect perfectly
- `centered composition` — Subject in middle
- `top-down orthographic view` — No perspective
- `isometric 45-degree angle` — For 3D-looking 2D
- `closeup macro detail` — Zoomed in
- `texture swatch, filling entire frame` — Edge-to-edge

**Examples:**
```
"flat, straight-on view, completely filling the frame"
"seamless tileable texture with edges that connect perfectly"
"top-down orthographic view showing the block's top surface"
```

### 5. Lighting (How light interacts)
Dramatically affects the final look.

**Lighting Types:**
- **Soft**: diffused, ambient, overcast, gentle
- **Hard**: direct sunlight, studio lighting, harsh shadows
- **Special**: rim lighting, backlighting, volumetric rays
- **Game**: flat lighting, cel-shaded, uniform illumination

**Direction**:
- Top-down, side lighting, three-quarter lighting, even omnidirectional

**Examples:**
```
"soft, diffused lighting from above with minimal shadows"
"even, flat lighting suitable for game textures"
"gentle ambient light with subtle directional shading from top-left"
```

### 6. Color Palette (Specific colors)
Don't just say "brown" - be precise!

**Formula**: `[saturation] [hue] [value]`

**Saturation**: vibrant, muted, desaturated, rich, pastel, bold
**Hue**: exact color names (ochre, sienna, cerulean, crimson)
**Value**: bright, dark, mid-tone

**Examples:**
```
"warm brown color palette ranging from sienna to dark umber"
"vibrant, saturated greens with emerald and lime accents"
"desaturated blue-gray stone colors with cool undertones"
"limited palette of 3-5 colors: bright green, yellow-green, brown, dark brown"
```

### 7. Mood/Atmosphere
Sets the emotional tone.

**Options:**
- cheerful, playful, friendly, cute, innocent
- serious, professional, realistic, authentic
- mysterious, magical, ethereal, enchanted
- gritty, weathered, aged, rustic
- clean, pristine, modern, minimalist

**Examples:**
```
"cheerful and playful mood suitable for children"
"rustic and natural atmosphere"
"magical and enchanted feeling with subtle mystical elements"
```

### 8. Technical Details (The fine-tuning)
This is where you get very specific.

**Resolution/Quality**:
```
"high-resolution, crisp edges"
"16x16 pixel dimensions with visible pixel grid"
"4K quality texture with fine detail"
```

**Material Properties**:
```
"non-reflective matte finish"
"slight specular highlights on raised areas"
"subsurface scattering in translucent areas"
```

**Style Constraints**:
```
"simplified geometric shapes, no photorealistic detail"
"exaggerated features for cartoon aesthetic"
"subtle variation, avoiding pure repetition"
"organic randomness within structured grid"
```

## Minecraft-Specific Prompt Templates

### Block Textures (16x16 or tileable)

```
A [style] seamless tileable texture of [material/block type], 
showing [3-5 key visual features], 
flat straight-on orthographic view filling the entire frame,
[lighting type] from above creating [shadow description],
[detailed color palette],
[mood/atmosphere],
optimized for [resolution], with [edge treatment] edges,
[style constraints]
```

**Example - Dirt Block:**
```
A cute cartoon-style seamless tileable texture of packed dirt and soil,
showing small rounded pebbles, subtle crack lines, and organic texture variation,
flat straight-on orthographic view filling the entire frame,
soft ambient lighting from above with gentle top-left directional shading,
warm earthy brown color palette ranging from light tan to rich chocolate brown,
friendly and approachable mood suitable for children's games,
optimized for 16x16 pixel base resolution but scalable,
with perfectly connecting edges for seamless tiling,
simplified geometric shapes with rounded features avoiding photorealism
```

### Item Textures (Icons/Tools)

```
A [style] [item type] icon texture,
showing [orientation/angle] with [key features],
centered composition on transparent or [color] background,
[lighting description] creating [highlight placement],
[color palette with accent colors],
[mood],
[size/resolution], [shading style], [outline treatment]
```

**Example - Diamond Sword:**
```
A vibrant cartoon-style diamond sword icon texture,
showing a straight vertical sword with cyan-blue diamond blade and dark brown leather-wrapped handle,
centered composition on transparent background,
dramatic top-right lighting creating bright highlights on the blade edge and pommel,
brilliant cyan-blue for blade with white sparkle accents, rich dark brown for handle with tan wrapping details,
heroic and powerful mood with magical quality,
designed for 16x16 base resolution with pixel-art precision,
cel-shaded style with bold outlines and distinct color zones,
2-pixel black outline for clarity against any background
```

### Ore Textures (Base + Embedded Material)

```
A [style] ore texture showing [ore material] embedded in [base stone],
with [distribution pattern] of [ore features],
[composition style],
[lighting on both materials],
[base color] stone with [ore color] mineral deposits,
[technical notes about depth/layers]
```

**Example - Diamond Ore:**
```
A photorealistic ore texture showing cyan diamond crystals embedded in dark gray cobblestone,
with 3-5 scattered diamond crystal clusters showing angular geometric facets,
asymmetric but balanced composition filling frame edge-to-edge,
subtle ambient lighting with bright internal reflections in diamond facets,
dark charcoal gray stone base with brilliant cyan-blue diamond crystals and white sparkle points,
mysterious and valuable mood suggesting rarity,
showing depth with darker recessed stone areas and lighter raised crystal surfaces,
optimized for seamless tiling with varied crystal placement near edges
```

## Advanced Techniques

### 1. Multi-Part Prompts (For Complex Textures)
Break down into sections:

```
Background: [base layer description]
Foreground: [top layer details]
Accents: [special features]
Overall: [unifying characteristics]
```

### 2. Negative Space Control
Instead of saying "no X", describe the space:

❌ "grass texture with no flowers"
✅ "uniform grass texture showing only grass blades in consistent pattern"

### 3. Reference Blending
When using reference images in batch config:

```
"Transform this texture to match [style description] while preserving 
[specific elements to keep], applying [changes to make], 
resulting in [final aesthetic]"
```

### 4. Aspect Ratio Considerations

For different texture types:
- **Square (1:1)**: Standard blocks, items
- **Wide (16:9)**: Panoramas, banners  
- **Tall (9:16)**: Vertical elements, signs

Adjust composition language:
```
"horizontal composition spreading across the width"
"vertical stack arrangement from top to bottom"
```

### 5. Style Consistency Formula

For maintaining consistent style across multiple textures:

```
Create a shared "style DNA" description:
"Cartoon aesthetic with: rounded edges on all shapes, 2-pixel outlines, 
simplified 3-4 color shading gradients, friendly exaggerated features, 
soft pastel color palette, minimal detail complexity"

Then append to each prompt:
"[specific texture description] + [style DNA]"
```

### 6. Iteration Refinement

Start broad, then add detail:

**Pass 1 (Basic):**
```
"Cartoon stone block texture"
```

**Pass 2 (Structure):**
```
"Cartoon stone block texture, gray color, rough surface, straight-on view"
```

**Pass 3 (Detail):**
```
"Cartoon-style seamless stone block texture, showing rough bumpy surface 
with angular cracks, light gray color with darker crevices, 
flat straight-on view, soft lighting, friendly mood"
```

**Pass 4 (Technical):**
```
"Cartoon-style seamless tileable stone block texture, showing rough bumpy surface 
with 4-6 angular geometric cracks creating irregular polygonal sections, 
light silver-gray primary color (RGB 180, 180, 180) with darker charcoal 
crevices (RGB 100, 100, 105), flat orthographic straight-on view filling frame, 
soft diffused lighting from top-left creating subtle gradient shading, 
friendly approachable mood for children's game, 16x16 optimized with 
perfectly connecting edges, simplified shapes with 2-pixel line weights"
```

## Quality Control Checklist

Before finalizing a prompt, verify:

- [ ] Medium/style is specified
- [ ] Subject is clearly defined  
- [ ] 3-5 key characteristics listed
- [ ] Composition/framing stated
- [ ] Lighting described
- [ ] Color palette detailed (not just "brown")
- [ ] Mood/atmosphere included
- [ ] Technical requirements specified
- [ ] Edge treatment mentioned (for tileables)
- [ ] Resolution/size noted
- [ ] Consistent with pack's overall style

## Common Minecraft Texture Patterns

### Pattern Library

Copy these proven formulas for common textures:

**Natural Blocks (dirt, sand, gravel):**
```
[style] seamless texture of [material], showing [particle type] with 
[size variation], [distribution pattern], flat view, [lighting], 
[earth-tone palette], natural organic mood, tileable edges
```

**Stone/Ore Blocks:**
```
[style] [stone type] texture with [feature pattern], showing [surface quality],
[crack/vein description], flat orthographic view, [lighting creating depth],
[gray/brown palette], [mood], seamless tileable
```

**Wood Blocks (logs, planks):**
```
[style] [wood type] texture displaying [grain pattern], [knot placement],
[color variation], [view angle], [lighting along grain], 
[wood-tone palette], [warm/natural mood], [edge treatment]
```

**Metal/Crystal:**
```
[style] [material] showing [surface quality], [reflection pattern],
[facet/edge description], [angle], [lighting with highlights],
[metallic/crystalline palette], [mood], [special effects]
```

**Organic (leaves, plants):**
```
[style] [plant type] texture with [leaf/element arrangement], 
[detail level], [transparency notes], [view], [natural lighting],
[green palette variation], [lively mood], [edge alpha handling]
```

## Pro Tips

1. **Use specific numbers**: "3-5 cracks" vs "some cracks"
2. **Name actual colors**: "burnt sienna" vs "reddish brown"  
3. **Reference art styles**: "Studio Ghibli style", "Pixar aesthetic"
4. **Specify what it's NOT**: "simplified, not photorealistic"
5. **Add context**: "suitable for children's game"
6. **Consider the pack**: Reference other textures for consistency
7. **Test and iterate**: Save prompts that work well
8. **Layer your descriptions**: Start general, add specifics
9. **Use industry terms**: PBR, albedo, normal map, etc. (if supported)
10. **Think like a photographer**: ISO, aperture, focal length (for realistic)

## Example: Full Process

**Goal**: Cartoon grass block top texture

**Step 1 - Define core elements:**
- Style: Cute cartoon
- Subject: Grass surface
- View: Top-down

**Step 2 - Add characteristics:**
- Small grass blades
- Flowers (2-3)
- Color variation
- Friendly appearance

**Step 3 - Technical details:**
- Seamless tileable
- Bright vibrant greens
- Soft lighting
- 16x16 optimized

**Step 4 - Complete prompt:**
```
A cheerful cartoon-style seamless tileable texture of a vibrant grass block top surface,
showing dense short grass blades with slight directional variation, 2-3 small 
simple flowers (yellow and white) scattered asymmetrically, subtle green color 
variation creating organic depth,
flat top-down orthographic view filling the entire frame edge-to-edge,
soft ambient daylight from above with gentle brightness variation across surface,
bright vivid green color palette (lime green #90EE90 to forest green #228B22) 
with small pops of yellow (#FFD700) and white (#FFFFFF) for flowers,
joyful sunny cheerful mood perfect for children's adventure game,
optimized for 16x16 pixel base with scalability to higher resolutions,
perfectly tileable edges with grass continuing seamlessly across boundaries,
simplified playful shapes avoiding photorealism, rounded soft edges on all elements,
3-color gradient shading maximum per grass blade
```

## Batch Config Integration

In your `texture_config.json`, you can now use these detailed prompts:

```json
{
  "textures": [
    {
      "name": "grass_top_pro",
      "type": "block",
      "prompt": "[your detailed prompt here]"
    }
  ]
}
```

## Resources & Inspiration

- **Color Tools**: coolors.co, color.adobe.com
- **Material References**: textures.com, polyhaven.com
- **Style References**: Pinterest, ArtStation (search "Minecraft texture")
- **Minecraft Wiki**: minecraft.wiki for canonical texture references

---

**Remember**: The Gemini models are smart and understand context. You don't need to include EVERY element from this guide in every prompt—use what makes sense for your specific texture. Start simple, test, then add detail where needed!
