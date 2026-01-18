export default function AnimatedBackground() {
  const symbols = ["🧠", "🫀", "🫁", "🩺", "💉", "🧬", "📊"];

  return (
    <div className="background">
      {/* Waves */}
      <div className="wave" />
      <div className="wave delay" />

      {/* Floating medical symbols */}
      {symbols.map((icon, index) => (
        <span
          key={index}
          className="symbol"
          style={{
            top: `${Math.random() * 100}%`,
            left: `${Math.random() * 100}%`,
            animationDelay: `${Math.random() * 8}s`,
            fontSize: `${22 + Math.random() * 14}px`,
          }}
        >
          {icon}
        </span>
      ))}
    </div>
  );
}
