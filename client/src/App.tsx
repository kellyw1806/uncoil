import { useStore } from "@nanostores/react"
import { $screen } from "./stores/global"
import Landing from "./screens/Landing";
import Form from "./screens/Form";

function App() {
  const screen = useStore($screen);

  return (
    <div className="h-dvh w-full bg-beige flex">
      {screen === "landing" && <Form />}
    </div>
  )
}

export default App