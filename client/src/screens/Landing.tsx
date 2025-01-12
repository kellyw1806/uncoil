import Coil from "../components/Coil";
import { $screen } from "../stores/global";
import { useState, useEffect } from "react";

export default function LandingPage() {
  const [showNavbar, setShowNavbar] = useState(false);

  // Detect scroll position to show the navbar
  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 100) {
        setShowNavbar(true);
      } else {
        setShowNavbar(false);
      }
    };
    
    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div className="w-full" >
      {/* Navbar that appears on scroll */}
      {/* {showNavbar && (
        <div className="fixed top-0 w-full bg-black text-white p-4">
          <nav className="flex justify-center gap-6">
            <a href="#section1" className="text-xl hover:text-gray-400">Section 1</a>
            <a href="#section2" className="text-xl hover:text-gray-400">Section 2</a>
            <a href="#section3" className="text-xl hover:text-gray-400">Section 3</a>
          </nav>
        </div>
      )} */}

      {/* Landing Section */}
      <div className="h-dvh w-full flex relative">
        <img src="./landing/background.jpg" className="h-full w-full object-cover" />
        <div className="absolute top-0 right-0 h-full w-1/3 bg-[#000000A0] flex flex-col items-center justify-center">
          <div className="flex flex-col gap-y-6">
            <div className="mx-8">
              <div className="flex">
                <h1 className="text-pinenut text-6xl font-lusitana-bold">uncoil</h1>
                <div className="w-1 h-full relative">
                  <Coil className="absolute left-[-8px] top-3 w-28 stroke-pinenut" />
                </div>
              </div>
              <h2 className="text-pinenut text-2xl font-lusitana-bold">the future of physiotherapy</h2>
            </div>
            <div className="w-full aspect-square relative flex flex-col items-center justify-center text-4xl font-lusitana">
              <div className="absolute top-0 left-0 bg-pinenut w-[85%] aspect-square rounded-full opacity-70" />
              <div className="absolute bottom-0 right-0 bg-sawdust w-[85%] aspect-square rounded-full opacity-70" />
              <p className="z-20">stretch.</p>
              <p className="z-20">correct.</p>
              <p className="z-20">relief.</p>
            </div>
            <div className="flex justify-center">
              <button
                className="bg-pinenut70 w-auto px-12 py-4 rounded-2xl text-xl font-lusitana text-beige hover:bg-pinenut transition-colors"
                onClick={() => $screen.set("form")}
              >
                Begin your journey!
              </button>
            </div>
          </div>
        </div>
      </div>

      <div id="section1" className="h-screen bg-sawdust relative">
        <img src="./landing/about1.png" className="absolute" style={{"top": "183px", "width": "670px", "height": "524px", "left": "3%"}} />
        <img src="./landing/about2.png" className="absolute" style={{"top": "357px", "right": "0%", "width": "378px", "height": "563px"}} />
        <div className="font-lusitana absolute" style={{"top": "150px", "right": "580px", "fontSize": "57px", "fontWeight": "bold"}}>
        Every move matters. 
        </div>
        <div className="font-lusitana absolute bg-pinenut" style={{"top": "280px", "right": " 480px", "fontSize": "38px", "width": "600px", "opacity":"0.7"}}>
        The line between recovery and reinjury is drawn by one key factor: proper form. 
        </div>
        <div className="font-lusitana absolute" style={{"top": "500px", "right": "480px", "fontSize": "28px", "width": "600px"}}>
        Through innovative software, we reimagine the future of physical therapy, transforming every movement into a step toward recovery and strength.        </div>
        <div className="font-lusitana absolute" style={{"top": "750px", "left": "50px", "fontSize": "40px", "width": "1300px"}}> 
          There, at the intersection of expertise and innovation, we will meet Uncoil reshaping how we move, heal, and thrive.
        </div>

      </div>
      <div id="section2" className="h-screen relative" style={{"backgroundColor": "#86938E"}}>
      <div className="font-inknut absolute" style={{"fontSize": "36px", "width": "400px", "left": "1250px", "top": "200px"}}>
        our technology
        </div>
      </div>
      <div id="section3" className="h-screen relative" style={{"backgroundColor": "#DFBC9C"}}>
        <h2 className="text-4xl font-bold font-inknut absolute" style={{"fontSize": "36px", "left": "700px", "top": "150px"}}>let's show you how it works</h2>
      </div>
    </div>
  );
}
