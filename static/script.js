const html5QrCode = new Html5Qrcode("preview");

html5QrCode.start(
    { facingMode: "environment" },
    {
        fps: 10,
        qrbox: 250
    },
    qrCodeMessage => {
        // redirect to hotel page
        window.location.href = `/hotel/${qrCodeMessage}`;
    },
    errorMessage => {
        console.log("QR scan error:", errorMessage);
    }
);