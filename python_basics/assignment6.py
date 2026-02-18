# Program to display a diamond, triangle
# Write a program to solve quadratic equations

def draw_triangle(n):
    """Draws a right-angled triangle of height n"""
    print(f"\n--- Drawing Triangle (Size: {n}) ---")
    for i in range(1, n + 1):
        print('*' * i)

def draw_diamond(n):
    """Draws a diamond shape with width n"""
    print(f"\n--- Drawing Diamond (Size: {n}) ---")
    # Upper half (including middle)
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    # Lower half
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# --- Main Program ---
# You can change these numbers to make the shapes bigger or smaller
size = 5
draw_triangle(size)
draw_diamond(size)
