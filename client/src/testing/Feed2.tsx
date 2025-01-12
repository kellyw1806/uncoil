import { Button } from "antd";
import { useState, useEffect, useRef } from "react";

export default function Capture2() {
  const [isCameraOn, setIsCameraOn] = useState(false);
  const videoRef = useRef<HTMLVideoElement>(null);
  const wsRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    if (isCameraOn) {
      wsRef.current = new WebSocket("ws://localhost:8000/ws/feed");
      wsRef.current.binaryType = "arraybuffer";
      wsRef.current.onmessage = (event) => {
        console.log('msg')
        const blob = new Blob([event.data], { type: "image/jpeg" });
        const url = URL.createObjectURL(blob);
        if (videoRef.current) {
          videoRef.current.src = url;
        }
      };
      wsRef.current.onclose = () => {
        setIsCameraOn(false);
      };
    } else {
      if (wsRef.current) {
        wsRef.current.close();
      }
    }
    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, [isCameraOn]);

  return (
    <div>
      <Button onClick={() => setIsCameraOn(true)}>Start Camera</Button>
      <Button onClick={() => setIsCameraOn(false)}>Close Camera</Button>
      <video ref={videoRef} autoPlay />
    </div>
  );
}