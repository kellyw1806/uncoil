import { useStore } from "@nanostores/react"
import { $plan, $screen } from "../stores/global"

export default function Debrief() {
    const plan = useStore($plan)
    console.log(plan)
    return (
        <div>
            <h1>The Plan</h1>
            {plan.exercise_program.map((ex, i) => (
                <p key={i}>{ex.exercise} (15s)</p>
            ))}
            <button onClick={() => $screen.set("feed")}>Start</button>
        </div>
    )
}