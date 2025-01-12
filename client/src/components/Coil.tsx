interface CoilProps {
  className?: string;
}

export default function Coil({ className }: CoilProps) {
  return (
    <svg width="143" height="31" viewBox="0 0 143 31" className={className} xmlns="http://www.w3.org/2000/svg">
      <path d="M3 20.9159C9.32686 23.9731 15.4482 26.7498 22.7782 26.7498C29.7135 26.7498 56.334 20.531 47.2731 8.64254C42.9118 2.92024 35.6815 7.08813 37.9468 13.6509C44.2629 31.9495 57.5413 30.5745 71.3928 21.5763C73.1193 20.4547 95.8549 4.62342 89.3486 3.13882C85.0184 2.15077 79.5938 6.60673 81.7911 11.1192C89.5932 27.1422 111.279 29.8624 125.85 24.108C130.711 22.1882 134.736 19.5351 140 18.9345" stroke-width="5" stroke-linecap="round" />
    </svg>
  )
}