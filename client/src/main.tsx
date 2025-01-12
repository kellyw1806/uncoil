import { ConfigProvider, theme } from "antd"
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ConfigProvider
      theme={{
        token: {
          colorPrimary: "#34d19e",
          borderRadius: 8,
        },
        algorithm: theme.darkAlgorithm,
      }}
    >

      <App />
    </ConfigProvider>
  </StrictMode>,
)
