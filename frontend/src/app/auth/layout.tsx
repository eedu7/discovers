import React from "react";

interface AuthLayoutProps {
    children: React.ReactNode;
}

function AuthLayout({ children }: AuthLayoutProps) {
    return (
        <div className="flex min-h-screen flex-col">
            <main className="grid flex-1">{children}</main>
        </div>
    );
}

export default AuthLayout;
