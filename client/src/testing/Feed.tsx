import { Button } from "antd";
import { useEffect, useRef, useState } from "react";

export default function Feed() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [mediaStream, setMediaStream] = useState<MediaStream | null>(null);
  const [socket, setSocket] = useState<WebSocket | null>(null);

  const startWebcam = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
      });
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
      }
      setMediaStream(stream);
    } catch (error) {
      console.error("Error accessing webcam", error);
    }
  };
  const stopWebcam = async () => {
    if (mediaStream) {
      mediaStream.getTracks().forEach((track) => {
        console.log("Stopping tracker", { track })
        track.stop();
      });
      setMediaStream(null);
    }
  };

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/feed");
    ws.onopen = () => {
      console.log("WebSocket connection opened");
    };
    ws.onclose = () => {
      console.log("WebSocket connection closed");
    };
    ws.onerror = (error) => {
      console.error("WebSocket error", error);
    };
    setSocket(ws);

    return () => {
      ws.close();
    };
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      if (!socket) return;
      if (socket.readyState !== WebSocket.OPEN) return;
      if (!mediaStream) return;
      if (!canvasRef.current) return;
      if (!videoRef.current) return;

      const video = videoRef.current;
      const canvas = canvasRef.current;
      const context = canvas.getContext("2d");

      if (!context) return;
      if (!video.videoWidth) return;
      if (!video.videoHeight) return;

      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
      const data = canvas.toDataURL("image/jpeg");
      socket.send(data);
      console.log("send data")
    }, 1000 / 15);
    return () => clearInterval(interval);
  }, [mediaStream, socket])

  return (
    <div>
      <canvas ref={canvasRef} className="hidden" />
      <div>
        <video
          ref={videoRef}
          autoPlay
          muted
          className="border-4 border-neutral-400 rounded-3xl aspect-[4/3] bg-black"
          style={{ width: "75%" }}
        />
      </div>
      <Button onClick={startWebcam}>Start Camera</Button>
      <Button onClick={stopWebcam}>Stop Camera</Button>
    </div>
  )
}