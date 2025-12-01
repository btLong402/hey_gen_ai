import streamlit as st
import streamlit.components.v1 as components

# --- 1. SETUP PAGE ---
st.set_page_config(
    page_title="HeyGen AI Space Core",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. DEEP SPACE UI & PARTICLE SYSTEM ---
def inject_space_css():
    st.markdown("""
        <style>
            /* IMPORT FONT */
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Exo+2:wght@300;600&display=swap');

            /* --- BACKGROUND: DEEP SPACE --- */
            .stApp {
                background-color: #000;
                background-image: 
                    radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
                    radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
                    radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 20px),
                    radial-gradient(circle at 50% 50%, rgba(20, 30, 50, 0.5) 0%, rgba(0,0,0,0) 70%);
                background-size: 550px 550px, 350px 350px, 250px 250px, 100% 100%;
                background-position: 0 0, 40px 60px, 130px 270px, center;
                animation: spaceMove 120s linear infinite;
            }
            
            @keyframes spaceMove {
                from { background-position: 0 0, 40px 60px, 130px 270px, center; }
                to { background-position: 550px 550px, 390px 410px, 380px 520px, center; }
            }

            /* --- PARTICLE CANVAS --- */
            #particle-canvas {
                position: fixed;
                top: 0; left: 0; width: 100%; height: 100%;
                pointer-events: none;
                z-index: 0; /* Đặt thấp nhất để không che Avatar */
                mix-blend-mode: screen;
            }

            /* UI CLEANUP */
            #MainMenu, footer, header {visibility: hidden;}
            .block-container { padding-top: 2rem; padding-bottom: 0rem; max-width: 100%; }

            /* TYPOGRAPHY */
            .space-title {
                font-family: 'Orbitron', sans-serif;
                text-align: center;
                font-size: 3rem;
                font-weight: 700;
                background: linear-gradient(to bottom, #fff, #87ceeb);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 20px rgba(135, 206, 235, 0.8);
                letter-spacing: 6px;
                margin-bottom: 5px;
                position: relative; z-index: 10;
            }
            .space-subtitle {
                font-family: 'Exo 2', sans-serif;
                text-align: center;
                color: #aaddff;
                font-size: 1rem;
                letter-spacing: 2px;
                opacity: 0.8;
                position: relative; z-index: 10;
            }
        </style>
        
        <canvas id="particle-canvas"></canvas>
        <script>
            /* --- PARTICLE SYSTEM LOGIC (Giữ nguyên hiệu ứng sao băng) --- */
            const canvas = document.getElementById('particle-canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            let particlesArray = [];
            const colors = ['#ffffff', '#87ceeb', '#e0ffff', '#b0e0e6'];

            window.addEventListener('resize', function(){
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            });
            const mouse = { x: undefined, y: undefined };
            window.addEventListener('mousemove', function(event){
                mouse.x = event.x;
                mouse.y = event.y;
                for (let i = 0; i < 3; i++) particlesArray.push(new Particle());
            });
            class Particle {
                constructor(){
                    this.x = mouse.x; this.y = mouse.y;
                    this.size = Math.random() * 3 + 1;
                    this.speedX = Math.random() * 2 - 1;
                    this.speedY = Math.random() * 2 - 1;
                    this.color = colors[Math.floor(Math.random() * colors.length)];
                    this.life = 1.0;
                }
                update(){
                    this.x += this.speedX; this.y += this.speedY;
                    if (this.size > 0.2) this.size -= 0.05;
                    this.life -= 0.02;
                }
                draw(){
                    ctx.fillStyle = this.color; ctx.globalAlpha = this.life;
                    ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fill(); ctx.globalAlpha = 1.0;
                }
            }
            function handleParticles(){
                for (let i = 0; i < particlesArray.length; i++){
                    particlesArray[i].update(); particlesArray[i].draw();
                    if (particlesArray[i].size <= 0.3 || particlesArray[i].life <= 0){
                        particlesArray.splice(i, 1); i--;
                    }
                }
            }
            function animate(){
                ctx.fillStyle = 'rgba(0,0,0,0.1)'; 
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                handleParticles();
                requestAnimationFrame(animate);
            }
            animate();
        </script>
    """, unsafe_allow_html=True)

# --- 3. HEYGEN COMPONENT (BUG FIXED VERSION) ---
def get_heygen_html_snippet():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>HeyGen AI</title>
      <style>
        /* Đảm bảo HTML/Body trong suốt hoàn toàn */
        body, html { margin: 0; padding: 0; background: transparent !important; overflow: hidden; height: 100%; width: 100%; }
        body { display: flex; justify-content: center; align-items: center; }
      </style>
    </head>
    <body>
      <script>
      !function(window){
          const host = "https://labs.heygen.com";
          const url=host+"/guest/streaming-embed?share=eyJxdWFsaXR5IjoiaGlnaCIsImF2YXRhck5hbWUiOiJKdW5lX0hSX3B1YmxpYyIsInByZXZpZXdJ%0D%0AbWciOiJodHRwczovL2ZpbGVzMi5oZXlnZW4uYWkvYXZhdGFyL3YzLzc0NDQ3YTI3ODU5YTQ1NmM5%0D%0ANTVlMDFmMjFlZjE4MjE2XzQ1NjIwL3ByZXZpZXdfdGFsa18xLndlYnAiLCJuZWVkUmVtb3ZlQmFj%0D%0Aa2dyb3VuZCI6ZmFsc2UsImtub3dsZWRnZUJhc2VJZCI6IjYxZGViMDRmMzdmZjRmMmVhMTY0ZGM3%0D%0AMDcyYjcwNWIyIiwidXNlcm5hbWUiOiI5NWJmMjIyOTk4NWQ0MWVlYjAwNWY3ZjUyNzVmZDZjZSJ9&inIFrame=1";

          const wrapDiv = document.createElement("div");
          wrapDiv.id = "heygen-streaming-embed";
          
          const container = document.createElement("div");
          container.id = "heygen-streaming-container";

          const stylesheet = document.createElement("style");
          stylesheet.innerHTML = `
          #heygen-streaming-embed {
              z-index: 2147483647; /* Lớp cao nhất có thể */
              position: absolute;
              top: 50%; left: 50%;
              transform: translate(-50%, -50%);
              
              /* TRẠNG THÁI THU GỌN: HÌNH TRÒN */
              width: 150px; height: 150px;
              border-radius: 50%;
              overflow: hidden; 
              
              /* Ảnh nền */
              background-image: url('https://files2.heygen.ai/avatar/v3/74447a27859a456c955e01f21ef18216_45620/preview_talk_1.webp');
              background-size: cover;
              background-position: center 20%;
              background-repeat: no-repeat;

              border: 3px solid rgba(135, 206, 235, 0.5);
              box-shadow: 0 0 40px rgba(135, 206, 235, 0.4);
              transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
              opacity: 0; visibility: hidden;
              cursor: pointer;
          }

          /* TRẠNG THÁI MỞ RỘNG (EXPAND) - SỬA LỖI Ở ĐÂY */
          #heygen-streaming-embed.expand {
              width: 100% !important; 
              height: 100% !important;
              max-width: 100% !important;
              max-height: 100% !important;
              
              border-radius: 0; /* Bỏ bo góc để full màn hình iframe */
              border: none;
              box-shadow: none;
              
              /* QUAN TRỌNG: Nền trong suốt thay vì màu đen */
              background: transparent; 
              background-image: none;
              
              /* Đặt lại vị trí để lấp đầy iframe */
              top: 0; left: 0;
              transform: none;
              overflow: visible; /* Cho phép nội dung hiển thị hết */
          }

          #heygen-streaming-container {
              width: 100%; height: 100%;
          }
          
          #heygen-streaming-container iframe { 
              width: 100%; height: 100%; 
              border: 0; 
              position: absolute; top:0; left:0;
          }
          
          #heygen-streaming-embed.show { opacity: 1; visibility: visible; }
          `;

          const iframe = document.createElement("iframe");
          iframe.allowFullscreen = false;
          iframe.title = "Streaming Embed";
          iframe.role = "dialog";
          iframe.allow = "microphone";
          iframe.src = url;

          let visible = false;
          let initial = false;

          window.addEventListener("message", (e) => {
              if (e.origin === host && e.data && e.data.type === "streaming-embed") {
                  if (e.data.action === "init") {
                      initial = true;
                      wrapDiv.classList.toggle("show", initial);
                  } else if (e.data.action === "show") {
                      visible = true;
                      wrapDiv.classList.toggle("expand", visible);
                  } else if (e.data.action === "hide") {
                      visible = false;
                      wrapDiv.classList.toggle("expand", visible);
                  }
              }
          });

          container.appendChild(iframe);
          wrapDiv.appendChild(stylesheet);
          wrapDiv.appendChild(container);
          document.body.appendChild(wrapDiv);
      }(globalThis);
      </script>
    </body>
    </html>
    """

# --- 4. MAIN APP ---
def main():
    inject_space_css()

    st.markdown('<div class="space-title">GALACTIC AI INTERFACE</div>', unsafe_allow_html=True)
    st.markdown('<div class="space-subtitle">SYSTEM ONLINE | INITIALIZING NEURAL LINK...</div>', unsafe_allow_html=True)

    # Avatar Section
    col1, col2, col3 = st.columns([1, 10, 1])
    with col2:
        # height=550 là chiều cao an toàn để hiển thị đầy đủ avatar bán thân
        components.html(get_heygen_html_snippet(), height=550, scrolling=False)

if __name__ == "__main__":
    main()