import { z } from "zod";

export const loginFormSchema = z.object({
    email: z.string().email(),
    password: z.string(),
});

export const registerFormSchema = z.object({
    username: z.string(),
    email: z.string().email(),
    password: z.string(),
});
