import { useEffect, useRef, useState } from "react"
import { FaPlay, FaStop } from "react-icons/fa6";

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
      console.log("Joining stream", { stream });
    } catch (error) {
      console.error("Error accessing webcam", error);
    }
  };
  const stopWebcam = async () => {
    if (mediaStream) {
      mediaStream.getTracks().forEach((track) => {
        console.log("Stopping track", { track })
        track.stop();
      });
      setMediaStream(null);
    }
  };

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/feed");
    ws.onopen = () => console.log("WebSocket connection opened");
    ws.onclose = () => console.log("WebSocket connection closed");
    ws.onerror = (error) => console.error("WebSocket error", error);
    ws.onmessage = (event) => {
      const playMessage = async () => {
        console.log("Playing message", { message: event.data });
        const utterance = new SpeechSynthesisUtterance(event.data);
        utterance.lang = "en-US";
        const voice = speechSynthesis.getVoices().find((voice) => voice.name === "Google US English");
        if (voice) utterance.voice = voice;
        speechSynthesis.speak(utterance);
      }
      playMessage();
    }
    setSocket(ws);

    return () => ws.close();
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
    }, 1000 / 10);
    return () => clearInterval(interval);
  }, [mediaStream, socket])

  return (
    <div className="h-dvh w-full bg-snow flex items-center justify-center">
      <div className="flex flex-col gap-2 items-center">
        <div className="h-[550px] aspect-[4/3]">
          <video
            ref={videoRef}
            autoPlay
            muted
            className="border-4 border-neutral-400 rounded-3xl aspect-[4/3] bg-black"
            style={{ width: "100%" }}
          />
          <canvas ref={canvasRef} className="hidden" />
        </div>
        <div className="flex gap-x-2">
          <button
            className="p-3 rounded-full bg-neutral-800 hover:bg-neutral-600 transition-colors"
            onClick={startWebcam}
          >
            <FaPlay className="text-snow" />
          </button>
          <button
            className="p-3 rounded-full bg-neutral-800 hover:bg-neutral-600 transition-colors"
            onClick={stopWebcam}
          >
            <FaStop className="text-snow" />
          </button>
        </div>
      </div>
    </div>
  )
}